#!/bin/bash
# $0 ISOFILE
#d=$(dirname "$*")
#c=$(basename "$*")
#pushd "$d"

if [ -e "${@/.iso/.chd}" ]; then
	echo "Skipping: "
	echo "$@" 
	ls -alh "${@/.iso/.chd}" 
	exit 0
fi


chdman createcd -i "$@" -o "${@/.iso/.chd}"

#popd 
echo
