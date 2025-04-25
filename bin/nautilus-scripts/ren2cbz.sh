#!/bin/bash
# eikeno

lines=$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
lines_c=$(echo "$lines" | wc -l)
lines=$(echo "$lines"  | cat -n | sed 's/^ *//g')

for l in $(seq 1 $lines_c); do
	cl=$(echo "$lines" | grep -w ^"$l" | sed "s/^$l//g" | sed 's/^\t*//g')
	[ -n "$cl" ] && mv "$cl" "${cl//.zip/.cbz
	}"
done
