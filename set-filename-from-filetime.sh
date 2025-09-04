#!/bin/bash

for f in `ls -1 *.AVI`; do
	time=`stat $f | grep Modify | cut -c 9-27`
	echo $time
	# 2007-01-03 18:18:56
	year=`echo $time | cut -c 1-4`
	echo $year
	month=`echo $time | cut -c 6-7`
	echo $month
	dayyy=`echo $time | cut -c 9-10`
	echo $dayyy
	hour=`echo $time | cut -c 12-13`
	minute=`echo $time | cut -c 15-16`
	second=`echo $time | cut -c 18-19`
	newname="VID_${year}${month}${dayyy}_${hour}${minute}${second}.avi"
	echo $newname
	mv $f $newname
done

