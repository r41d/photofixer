#!/usr/bin/env python3

FOLDER = "setter"
ACTIVE = 1

LENS_VENDOR = "7artisans"
LENS_PRODUCT = "Fisheye"
LENS_FOCAL = 7.5 # 9mm
LENS_APERTURE = 2.8 # f/2.8 # wir gehen jetzt einfach mal davon aus dass die maximale Blende immer benutzt wurde...
CROP_FACTOR = 2

from set_lens_tags import set_lens_tags

set_lens_tags(FOLDER, ACTIVE, LENS_VENDOR, LENS_PRODUCT, LENS_FOCAL, LENS_APERTURE, CROP_FACTOR)
