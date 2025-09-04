# photofixer
Scripts/library for fixing up photos - work in progress

Mainly made for my own use, glad if it helps others

## Python EXIF library overview
Section added not because it brings me joy but because it's important to know this to not end up confused...
There are a lot of python EXIF libaries, many can do some things better than others, some of them want to be imported by the same name, it sometimes gets complicated.

- https://exiftool.org -> Not a python lib but THE command line tool for everything to do with EXIF
- https://exiv2.org -> Another tool, mentioned for completeness’s sake
- https://pypi.org/project/pyexif -> Imported as `pyexif`, Bad (as in no) documentation, last update 3 years ago (as of September 2025), not even a link to the source code, basically just wraps `exiftool`, but the `ExifEditor` class is kind of nice to use
- https://pypi.org/project/piexif -> Imported as `piexif`, Documentation and source is there, last update 6 years ago (as of September 2025), doesn't wrap `exiftool`, dealing with the dicts that you get is kind of cryptic (e.g. `piexif.load(file_path)["0th"][272]` gets you the camera model).
- https://pypi.org/project/PyExifTool -> Imported as `exiftool`, obviously wraps `exiftool`, main component is the `ExifToolHelper` class
- https://pypi.org/project/exif -> Imported as `exif`, doesn't seem to have a lot of activity, didn't try it yet
- https://pypi.org/project/exiv2 -> imported as `exiv2`, didn't try it yet
- https://pypi.org/project/pyexiv2 -> Imported as `pyexiv2` (CONFLICT!), wraps exiv2, development ceased?
- https://pypi.org/project/py3exiv2 -> Imported as `pyexiv2` (CONFLICT!), Debian/Ubuntu package is called `python3-py3exiv2`, wraps exiv2, the `ImageMetadata` class is kind of nice, but you're mostly left with reading the exiv2 documentation and guessing how to do it in the wrapping library
- https://pypi.org/project/python-xmp-toolkit -> as I understood it (am not an expert) XMP sometimes extends or complements EXIF, at least this library exposes some EXIF properties (e.g.: `xmpDict.get_property(consts.XMP_NS_EXIF, 'exif:DateTimeOriginal')`) but it's probably not the best tool here
