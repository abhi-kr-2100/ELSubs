#!/bin/sh

mkdir -p $1 $1/$1-FRAMES $1/$1-FRAMES/top $1/$1-FRAMES/bottom
yt-dlp -o $1/$1.video -f bestvideo[height=480] http://youtube.com/watch?v=$1
ffmpeg -i $1/$1.video -vf fps=0.5 $1/$1-FRAMES/frame_%05d.jpeg

for f in $1/$1-FRAMES/frame_*; do convert $f -crop 854x35+0+375 -threshold 55% -negate $1/$1-FRAMES/top/`basename $f`; done
for f in $1/$1-FRAMES/frame_*; do convert $f -crop 854x25+0+410 -threshold 55% -negate $1/$1-FRAMES/bottom/`basename $f`; done

ls -d -1 $1/$1-FRAMES/top/*.jpeg | tesseract - - -l $2 -c page_separator="" | cat > $1/$1.top.txt
ls -d -1 $1/$1-FRAMES/bottom/*.jpeg | tesseract - - -l eng -c page_separator="" | cat > $1/$1.bottom.txt

dedupe.py $1/$1.top.txt $1/$1.bottom.txt
sentencify.py $1/$1.top.txt $1/$1.bottom.txt
