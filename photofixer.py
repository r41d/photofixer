#!/usr/bin/env python3

import os

import photofixerconfig
from photoclass import Photo
from read_tags import read_tags
from mover import move_file

INPUT = "pic-input"
OUTPUT = "pic-sorted"

# 0 = Copy; 1 = Move
MOVE = 0

# TODO: implement various modes:
# Optionally fetch from external storage (camera/SD) ...
# rename in-place
# rename and copy
# rename and move
# ... optionally upload (rclone)

if __name__ == "__main__":
    print("Starting photofixer")

    for filename in os.listdir(INPUT):
        photo: Photo = Photo(INPUT, filename)

        if not (os.path.isfile(photo.filepath) and photo.ext.upper() in photofixerconfig.EXTENSIONS):
            # skip everything that is not a file or doesn't have one of the extensions we're interested in
            print("Skipping {}".format(photo.filename))
            continue

        try:
            photo.make, photo.model, photo.dt = read_tags(photo.filepath)

        except Exception as e:
            print(f"Error handling {photo.filename}:", e)
            continue

        photo.sanitize_model()

        photo.newname = f"{photo.dt.strftime('%Y%m%d')}_{photo.dt.strftime('%H%M%S')}_{photo.model}_{photo.base}.{photo.ext}"

        print(photo.filename, photo.model, photo.dt, "->", photo.newname)

        move_file(photo, OUTPUT, MOVE)
