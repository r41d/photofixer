#!/usr/bin/env python3

import os, pwd, glob, shutil
import datetime
import itertools
#import pprint
import pyexiv2 # pip install pyexiv2
from rclone_python import rclone # pip install rclone-python
from rclone_python.remote_types import RemoteTypes

ROOT = os.path.join("/media", pwd.getpwuid(os.getuid()).pw_name)
EXTENSIONS = [".JPG", ".RW2", ".ORF", ".ARW", ".DNF"]
OUTPUT = "pic-sorted"
MOVE = 0

sciebo = rclone.create_remote('sciebo', RemoteTypes.webdav)

if __name__ == "__main__":

    DCIMs = glob.glob(os.path.join(ROOT, "*", "DCIM"))
    if not DCIMs:
        print("no DCIM folders found")
        exit(0)

    files = []
    for ext in EXTENSIONS:
        new = [glob.glob(os.path.join(d, "**", f"*{ext}")) for d in DCIMs]
        files.extend(list(itertools.chain.from_iterable(new)))
    print(files)

    for file_path in files:
        try:
            folder, file = os.path.split(file_path)
            base, ext = os.path.splitext(file)
            ext = ext.lstrip('.').lower()
            
            exif = pyexiv2.Image(file_path).read_exif()
            #pprint.pprint(exif)
            make = exif["Exif.Image.Make"]
            model = exif["Exif.Image.Model"]
            dt = datetime.datetime.strptime(exif["Exif.Image.DateTime"], "%Y:%m:%d %H:%M:%S")
            
        except Exception as e:
            print("Error handling", file, e)
            continue

        newname = f"{dt.strftime('%Y%m%d_%H%M%S')}_{model}_{base}.{ext}"
        print(file, "→", newname)

        dest = os.path.join(OUTPUT, newname)
        if os.path.exists(dest):
            print("destination already exists, skipping", dest)
        else:
            func = shutil.move if MOVE else shutil.copy2
            func(file_path, dest)
