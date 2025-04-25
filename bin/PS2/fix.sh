#!/bin/bash



for i in *.chd; do
CUEFILE="${i/.chd/.cue}"
BINFILE="${i/.chd/.bin}"
echo "CUEFILE = $CUEFILE"
echo "BINFILE = $BINFILE"
echo "extracting $BINFILE: "
chdman extractcd --force -i "$i" -o "$CUEFILE" || continue
TAG=$(strings -a "$BINFILE" |egrep -i ^"(SLPM|SLUS|SCUS|SLES|SCES)" | head -n 1 | awk '{print $1}'|cut -f1 -d';'|sed 's/_//'|sed 's/\.//g' )
echo "TAG = $TAG"
echo
done


