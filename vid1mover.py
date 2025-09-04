#!/usr/bin/env python3

import os, shutil
import datetime
import pprint

import iso8601 # pip install iso8601
import zoneinfo # pip install tzdata

import exiftool # pip install PyExifTool / apt install exiftool
# import ffmpeg # pip install ffmpeg-python
# from libxmp import XMPFiles, consts # pip3 install python-xmp-toolkit
# from bs4 import BeautifulSoup

INPUT = "vid-input"
OUTPUT = "vid-sorted"
EXTENSIONS = (
    "MTS", # Panasonic DMC-GF1
    "MOV", # Olympus OM-D E-M10
    "MP4", # Sony DSC-RX100M5A / DSC-RX100M6 / ILCE-6000 / ILCE-6600 / ILCE-7M3
)
MOVE = 1

if __name__ == "__main__":
    for file in os.listdir(INPUT):
        file_path = os.path.join(INPUT, file)

        if not os.path.isfile(file_path):
            continue

        folder, file = os.path.split(file_path)
        base, ext = os.path.splitext(file)
        ext = ext.lstrip('.')#.lower()

        if not ext in EXTENSIONS:
            continue

        print('-', file_path)

        with exiftool.ExifToolHelper() as et:
            meta = et.get_metadata(file_path)[0]
            try:
                date = meta["XML:CreationDateValue"]
                dt = datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S%z")
            except:
                try:
                    date = meta["QuickTime:CreateDate"]
                    dt = datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
                    dt = dt.astimezone(zoneinfo.ZoneInfo("Europe/Berlin")) # man darf nur hoffen dass das für Sommerzeit tut
                except:
                    date = meta["File:FileModifyDate"] # das sollte es eigentlich immer geben
                    dt = datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S%z")

            try:
                model = meta["XML:DeviceModelName"]
            except:
                mapping = {"mts": "Panasonic", "mov": "Olympus", "mp4": "Sony"}
                model = mapping[ext]

        newname = f"{dt.strftime('%Y%m%d_%H%M%S')}_{model}_{base}.{ext}"

        print("  -", file, model, dt, newname)

        dest = os.path.join(OUTPUT, newname)
        if os.path.exists(dest):
            print("  - destination already exists, skipping", dest)
        else:
            func = shutil.move if MOVE else shutil.copy2
            func(file_path, dest)

