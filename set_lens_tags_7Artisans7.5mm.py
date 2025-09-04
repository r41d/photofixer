#!/usr/bin/env python3

import os, datetime
import pyexif

FOLDER = "setter"
EXTENSIONS = [".JPG", ".RW2", ".ORF", ".ARW", ".DNF"]

LENS_VENDOR = "7artisans"
LENS_PRODUCT = "Fisheye"
LENS_FOCAL = 7.5 # 9mm
LENS_APERTURE = 2.8 # f/2.8 # wir gehen jetzt einfach mal davon aus dass die maximale Blende immer benutzt wurde...

ACTIVE = 1

def batch_set(metadata, value, tags):
    for tag in tags:
        metadata.set_tag(tag, value)

if __name__ == "__main__":
    for file in os.listdir(FOLDER):
        file_path = os.path.join(FOLDER, file)
        if not(os.path.isfile(file_path) and os.path.splitext(file)[1].upper() in EXTENSIONS):
            continue

        try:
            metadata = pyexif.pyexif.ExifEditor(file_path)

            if metadata.get_tag("FocalLength") in ['0.0 mm', '1.0 mm'] and metadata.get_tag("MaxAperture") == 0.0:
                print(file_path, "found one")
            else:
                print(file_path, "nope:", metadata.getTags())
                continue

            metadata.set_tag("FocalLength", f"{LENS_FOCAL:0.1f} mm")
            metadata.set_tag("FocalLength35efl", f"{LENS_FOCAL:0.1f} mm (35 mm equivalent: {2*LENS_FOCAL:0.1f} mm)")
            batch_set(metadata, LENS_FOCAL, ["MaxFocalLength", "MinFocalLength"])

            batch_set(metadata, LENS_APERTURE, ["FNumber", "Aperture",
                "MaxAperture", "MaxApertureValue", "MaxApertureAtMinFocal", "MaxApertureAtMaxFocal"])

            metadata.set_tag("LensInfo", f"{LENS_FOCAL}mm f/{LENS_APERTURE}") # "20mm f/1.7"
            metadata.set_tag("LensModel", f"{LENS_PRODUCT} {LENS_FOCAL}/F{LENS_APERTURE}") # "LUMIX G 20/F1.7"
            metadata.set_tag("LensType", f"{LENS_PRODUCT} {LENS_FOCAL}mm F{LENS_APERTURE}") # "Lumix G 20mm F1.7 Asph."
            # LensID -> Warning: Expected one or more integer values in XMP-aux:LensID (ValueConvInv)

            print(metadata.getTags())

        except ValueError:
            print("Error handling", file)
            continue

        #print(file, make, model, dt)
