#!/usr/bin/env python3

import os
import shutil
import datetime

import photofixerconfig


def move_file(photo, OUTPUT: str, MOVE):
    if photo.dt.hour < photofixerconfig.NEW_DAY_STARTS_AT_HOUR:  # it is before this time, we put the file in the previous day's folder
        photo.dt -= datetime.timedelta(days=1)
    destdir = os.path.join(OUTPUT, photo.dt.strftime('%Y-%m-%d'))
    os.makedirs(destdir, exist_ok=True)
    dest = os.path.join(destdir, photo.newname)
    if os.path.exists(dest):
        print("destination already exists, skipping", dest)
    else:
        func = shutil.move if MOVE else shutil.copy2
        func(photo.filepath, dest)
