
import re

import photoclass





def attempt_camera_filename(photo: photoclass.Photo):
    # 8 chars + .JPG
    p = re.compile("([A-Z0-9_]{8}).([A-Za-z]{3})")
    m = p.match(photo.filename)
    if m:
        base, ext = m.groups()
        print('Match found: ', m.groups())
    else:
        print('No match')
    pass

def attempt_photofixer_filename(photo: photoclass.Photo):
    # Generated like this:
    # photo.newname = f"{photo.dt.strftime('%Y%m%d')}_{photo.dt.strftime('%H%M%S')}_{photo.model}_{photo.base}.{photo.ext}"

    p = re.compile("(\d{4}\d{2}\d{2})_(\d{2}\d{2}\d{2})_([A-Za-z0-9-_]*)_([A-Z0-9_]{8}).([A-Za-z]{3})")
    m = p.match(photo.filename)
    if m:
        Ymd, HMS, model, base, ext = m.groups()
        print('Match found: ', m.groups())
    else:
        print('No match')
    pass


def attempt_smartphone_filename(photo: photoclass.Photo):
    # Examples:
    # 20250831_185059.heic            <- normal
    # 20250831_152622_001.jpg         <- burst shot
    # 20240427_013518(0).jpg          <- mehrere Fotos in derselben Sekunde
    # 20240724_124048~2.jpg           <- ich glaub das ist was editiertes

    p = re.compile("(\d{4}\d{2}\d{2})_(\d{2}\d{2}\d{2})((_\d*)?(~\d*)?(\(\d*\))?).([A-Za-z]{3,4})")
    m = p.match(photo.filename)
    if m:
        Ymd, HMS, ext = m.groups()
        print('Match found: ', m.groups())
    else:
        print('No match')
    pass

def attempt_pixel(photo: photoclass.Photo):
    # IMPORTANT: Filename are UTC, not local time; OriginalDateDigitized in EXIF is in local time
    # Die Pixel haben außerdem Millisekunden im Filename, aber nicht in den EXIF Daten...
    # Examples:
    # PXL_20230812_005706479.jpg
    # PXL_20250901_114747712.MP.jpg

    p = re.compile("PXL_(\d{4}\d{2}\d{2})_(\d{2}\d{2}\d{2})(\d{3})(?:.MP)?.([A-Za-z]{3,4})")
    m = p.match(photo.filename)
    if m:
        Ymd, HMS, ms, ext = m.groups()
        print('Match found: ', m.groups())
    else:
        print('No match')
    pass
