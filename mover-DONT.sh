#!/usr/bin/env bash

# Old mover script, use the python version now

MOVE=1

declare -a EXTENSIONS=("JPG" "RW2" "ORF" "ARW" "DNF")

find . -type d -name pic-input | while read inputDir; do
#find /media/ -type d -name DCIM | while read inputDir; do

    for EXT in "${EXTENSIONS[@]}"; do

        # -iname for case-insensitive
        find "$inputDir" -type f -iname "*.$EXT" -print0 | while IFS= read -r -d '' original; do

            daydir=$(exiftool -T -createdate -d "%Y-%m-%d" "$original")
            if [[ $(exiftool -T -createdate -d "%H" "$original") -lt 6 ]]; then
                daydir=$(date -d "${daydir} - 1day" --iso-8601)
            fi
            dest=pic-sorted/${daydir}
            mkdir -p $dest

            basefile=$(basename -- "$original") # only filename without full path
            base="${basefile%.*}" # extension cropped
            ext=$(echo "${basefile#*.}" | tr '[:upper:]' '[:lower:]') # always make ext lowercase
            Ymd=$(exiftool -T -DateTimeOriginal -d "%Y%m%d" "$original") # date with 8 letters
            HMS=$(exiftool -T -DateTimeOriginal -d "%H%M%S" "$original") # time with 6 letters
            Model=$(exiftool -Model -b "$original") # Camera Model (without vendor)
            NewPathName="${dest}/IMG_${Ymd}_${HMS}_${base}.${ext}"

            if [[ $MOVE -eq 1 ]]; then
                echo -e "Moving $original\n    to $NewPathName"
                mv "$original" "$NewPathName"
            else
                echo -e "Copying $original\n     to $NewPathName"
                cp "$original" "$NewPathName"
            fi

        done # file iteration

    done # extension iteration

done # DCIM dir iteration
