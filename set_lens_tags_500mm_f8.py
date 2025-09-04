#!/usr/bin/env python3

import sys

FOLDER = "setter"
ACTIVE = 1

LENS_VENDOR = "Danubia"
LENS_PRODUCT = "Tele"
LENS_FOCAL = 500 # 500mm
LENS_APERTURE = 8 # wir gehen jetzt einfach mal davon aus dass immer die maximale Blende immer benutzt wurde...
CROP_FACTOR = float(sys.argv[1])

from set_lens_tags import set_lens_tags

set_lens_tags(FOLDER, ACTIVE, LENS_VENDOR, LENS_PRODUCT, LENS_FOCAL, LENS_APERTURE, CROP_FACTOR)
