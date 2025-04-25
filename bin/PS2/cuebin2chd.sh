#!/bin/bash
# $0 CUEFILE
d=$(dirname "$*")
c=$(basename "$*")
pushd "$d"

chdman createcd -i "$c" -o "${c/.cue/.chd}"

popd 
echo
