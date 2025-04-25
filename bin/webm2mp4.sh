#!/bin/bash
# $@ foo.webm
# depends : ffmpeg

ffmpeg -i "$@" -c copy "${@/.webm/.mp4}"
