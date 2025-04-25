#!/bin/sh

if [ $# != 2 ]; then
	echo "$(basename $0) CUEFILE FLACFILE"
	exit 1
fi

shntool split -f $1 -o 'flac flac --output-name=%f -' -t '%n-%p-%t' $2



