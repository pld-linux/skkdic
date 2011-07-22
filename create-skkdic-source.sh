#!/bin/sh

DATE=$(date '+%Y%m%d')

mkdir -p skkdic-$DATE
cd skkdic-$DATE
wget -N -r -nH -np --cut-dirs=3 \
	-R 'index.html*' \
	-R '*.gz' -R '*.gz.md5' \
	http://openlab.ring.gr.jp/skk/skk/dic/
rm -rf robots.txt
cd .. && tar cvfj skkdic-${DATE}.tar.bz2 skkdic-$DATE

