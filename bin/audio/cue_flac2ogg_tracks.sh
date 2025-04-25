#!/bin/sh

if [ $# != 2 ]; then
	echo "$(basename $0) CUEFILE FLACFILE"
	exit 1
fi

shntool split -f $1 -o 'flac flac --output-name=%f -' -t '%n-%p-%t' $2

echo "Press any Key to delete $2 and convert \*.flac tracks to oog"
read foo

rm -f "$2"
find -name "*.flac" -exec oggenc -q7 "{}" \;

