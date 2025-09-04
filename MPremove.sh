#!/bin/bash

# Delete videos from MP files from Google Pixels (output file has "clean" in the filename)

for mp in `ls -1 PXL_*.MP.jpg`; do
	# Find out where in the file the video part starts
	# old string: "\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34\x32"
	extractposition=$(grep --binary --byte-offset --only-matching --text -P "\x00\x00\x00\x1c\x66\x74\x79\x70\x69\x73\x6f\x6d" $mp | sed 's/^\([0-9]*\).*/\1/')
	# Extract only the image
	dd if="$mp" count=1 bs=$extractposition of="$(basename -s .MP.jpg $mp).clean.jpg"
done
