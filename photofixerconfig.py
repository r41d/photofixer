
EXTENSIONS = [
    "JPG", "JPEG", "TIF", "TIFF", "HIF", "HEIF", "HEIC",  # non-raw pictures
    "DNG", "RAW",  # "universal" raw extensions
    "CRW", "CR2", "CR3",  # Canon
    "RAW",  # Fujifilm
    "3FR", "FFF",  # Hasselblad
    "DCR", "DCS", "KDC",  # Kodak
    "RWL",  # Leica
    "MRW", "MDC",  # Minolta
    "NEF", "NRW",  # Nikon
    "ORF", "ORI",  # Olympus
    "RW2",  # Panasonic
    "PEF",  # Pentax
    "SRW",  # Samsung
    "X3F",  # Sigma
    "ARW", "SRF", "SR2",  # Sony
    # "XMP", "PP3",  # metadata, raw editor stuff
]

# Set at 0 to have files after midnight going to the next folder (default: 6am)
NEW_DAY_STARTS_AT_HOUR = 6

# e.g. Samsung cameras have unnecessary (!) leading "SAMSUNG " in the Model
TRIM_MAKE_FROM_MODEL = True

# Possibility to fix stuff or deviate from EXIF entry for nicer(/shorter) filenames (at the expense of "falsifying" them)
MODEL_RENAMINGS = {
    "DSC-RX100": "RX100",  # RX100 1"-type models
    "WB35F/WB36F/WB37F": "WB37F",  # I know what I have, but sadly they were too lazy to be specific in the EXIF data -_-
}
