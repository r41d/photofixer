#!/usr/bin/env python3

FOLDER = "setter"
ACTIVE = 1

LENS_VENDOR = "Olympus"
LENS_PRODUCT = "Body Cap Lens"
LENS_FOCAL = 9 # 9mm
LENS_APERTURE = 8 # f/8, das Ding kann nichts anderes
CROP_FACTOR = 2

from set_lens_tags import set_lens_tags

set_lens_tags(FOLDER, ACTIVE, LENS_VENDOR, LENS_PRODUCT, LENS_FOCAL, LENS_APERTURE, CROP_FACTOR)
