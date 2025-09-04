cd vid-sorted
for vid in `ls -1 *.MP4`; do
	ffmpeg -i ${vid} -c:v libx265 -vtag hvc1 -crf 22 -c:a aac $(basename -s .MP4 ${vid})_hevc+aac_crf22.mp4
done

