#!/bin/sh
today=20`date +"%y-%m-%d"`
title=$1
pythontitle=$2
filename=$today-$title.md
touch $filename

python init_post.py $filename "$pythontitle"