#!/bin/bash

for i in *.iso; do

	if [ -f "${i/.iso/.chd}" ]; then
		echo "# Deleting already converted $i"
		rm -f "$i" || exit 3
		
	else
		echo "needs conversion $i"
	fi
done


