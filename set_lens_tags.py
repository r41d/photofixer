#!/usr/bin/env python3

import os

import pyexif  # it's this one -> https://pypi.org/project/pyexif
# TODO: migrate to py3exiv2

from photofixerconfig import EXTENSIONS


def batch_set(metadata, value, tags):
    for tag in tags:
        metadata.set_tag(tag, value)


def set_lens_tags(FOLDER: str, ACTIVE, LENS_VENDOR: str, LENS_PRODUCT: str, LENS_FOCAL: int, LENS_APERTURE: int, CROP_FACTOR=1):
    for file in os.listdir(FOLDER):
        file_path = os.path.join(FOLDER, file)
        if not (os.path.isfile(file_path) and os.path.splitext(file)[1].upper() in EXTENSIONS):
            continue

        try:
            metadata = pyexif.pyexif.ExifEditor(file_path)

            if metadata.get_tag("FocalLength") in ['0.0 mm', '1.0 mm'] and metadata.get_tag("MaxAperture") == 0.0:
                print(file_path, "found one")
            else:
                print(file_path, "nope:", metadata.getTags())
                continue

            metadata.set_tag("FocalLength", f"{LENS_FOCAL:0.1f} mm")
            metadata.set_tag("FocalLength35efl", f"{LENS_FOCAL:0.1f} mm (35 mm equivalent: {CROP_FACTOR * LENS_FOCAL:0.1f} mm)")
            batch_set(metadata, LENS_FOCAL, ["MaxFocalLength", "MinFocalLength"])

            batch_set(metadata, LENS_APERTURE, ["FNumber", "Aperture", "MaxAperture", "MaxApertureValue", "MaxApertureAtMinFocal", "MaxApertureAtMaxFocal"])

            metadata.set_tag("LensInfo", f"{LENS_FOCAL}mm f/{LENS_APERTURE}")  # "20mm f/1.7"
            metadata.set_tag("LensModel", f"{LENS_PRODUCT} {LENS_FOCAL}/F{LENS_APERTURE}")  # "LUMIX G 20/F1.7"
            metadata.set_tag("LensType", f"{LENS_PRODUCT} {LENS_FOCAL}mm F{LENS_APERTURE}")  # "Lumix G 20mm F1.7 Asph."
            # LensID -> Warning: Expected one or more integer values in XMP-aux:LensID (ValueConvInv)

            print(metadata.getTags())

        except ValueError:
            print("Error handling", file)
            continue
