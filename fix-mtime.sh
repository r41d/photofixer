#!/bin/bash

# IMG
for f in `ls -1 IMG_*`; do
	date=`echo $f | cut -c 5-12`
	hm=`echo $f | cut -c 14-17`
	s=`echo $f | cut -c 18-19`
	touch -t $date$hm.$s $f
done

# VID
for f in `ls -1 VID_*`; do
	date=`echo $f | cut -c 5-12`
	hm=`echo $f | cut -c 14-17`
	s=`echo $f | cut -c 18-19`
	touch -t $date$hm.$s $f
done

