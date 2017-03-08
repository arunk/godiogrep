#!/bin/bash

for f in ./video/*.mp4; do
    filename=${f##*/}
    name=${filename%.*}
    if [ ! -f ./audio/$name.mp3 ]; then
        ffmpeg -i $f ./audio/$name.mp3
    fi
    if [ ! -f ./audio/$name.mp3.transcription.txt ]; then
        cd audio && audiogrep --input $name.mp3 --transcribe && cd ..
    fi
done
