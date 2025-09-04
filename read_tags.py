import pyexiv2


def read_tags(file_path: str):
    exif = pyexiv2.ImageMetadata(file_path)
    exif.read()
    make = exif["Exif.Image.Make"].value.strip()
    model = exif["Exif.Image.Model"].value.strip()
    dt = exif["Exif.Image.DateTime"].value
    return make, model, dt
