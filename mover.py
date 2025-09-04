#!/usr/bin/env python3

import os, shutil
import datetime

import piexif
#import dateutil.parser

INPUT = "pic-input"
OUTPUT = "pic-sorted"
EXTENSIONS = [".JPG", ".RW2", ".ORF", ".ARW", ".DNF"]

MOVE = 1

if __name__ == "__main__":
    for file in os.listdir(INPUT):
        file_path = os.path.join(INPUT, file)
        if not(os.path.isfile(file_path) and os.path.splitext(file)[1].upper() in EXTENSIONS):
            continue

        try:
            base = os.path.splitext(file)[0]
            ext = os.path.splitext(file)[1].lstrip('.').lower()
            exif_dict = piexif.load(file_path)
            make = exif_dict["0th"][271].strip().decode('ascii').replace('/', '_')
            model = exif_dict["0th"][272].strip().decode('ascii').replace('/', '_')
            #time = exif_dict["0th"][306].strip().decode('ascii')
            time = exif_dict["Exif"][36867].decode('ascii') # 36867=DateTimeOriginal 36868=DateTimeDigitized
            dt = datetime.datetime.strptime(time, "%Y:%m:%d %H:%M:%S")

            #xmpDict = XMPFiles(file_path=file_path, open_forupdate=False).get_xmp()
            #dt = dateutil.parser.parse(xmpDict.get_property(consts.XMP_NS_EXIF, 'exif:DateTimeOriginal'))

        except Exception as e:
            print("Error handling", file, e)
            continue

        if make in model:
            model = model.replace(make, "").strip()

        newname = f"{dt.strftime('%Y%m%d')}_{dt.strftime('%H%M%S')}_{model}_{base}.{ext}"

        print(file, make, model, dt, newname)

        if dt.hour < 6: # it is before 6 am, we put the file in the previous day's folder
            dt -= datetime.timedelta(days=1)
        destdir = os.path.join(OUTPUT, dt.strftime('%Y-%m-%d'))
        os.makedirs(destdir, exist_ok=True)
        dest = os.path.join(destdir, newname)
        if os.path.exists(dest):
            print("destination already exists, skipping", dest)
        else:
            func = shutil.move if MOVE else shutil.copy2
            func(file_path, dest)

