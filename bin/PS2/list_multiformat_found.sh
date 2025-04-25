#!/bin/bash

for i in *.iso; do
	if [ -f "${i/.iso/.chd}" ]; then
		echo "# ISO and CHD found for $i"
	fi
done

for i in *.7z; do
	if [ -f "${i/.7z/.chd}" ]; then
		echo "# 7Z and CHD found for $i"
	fi
done

for i in *.iso; do
	if [ -f "${i/.iso/.7z}" ]; then
		echo "# 7Z and CHD found for $i"
	fi
done


