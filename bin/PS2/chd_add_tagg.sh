#!/bin/bash
# $0 CHD FILE
rm -f /tmp/binfile
rm -f /tmp/binfile.bin

CHD="$*"
BINFILE="${CHD/.chd/.bin}"

echo ">>>> Extracting $BINFILE"
chdman extractcd --force -i "$*" -o /tmp/binfile || exit 3

TAG=""
TAG=`strings /tmp/binfile.bin | grep ^SLUS_ | head -n1 | cut -f1 -d';' | sed -e 's/_//' -e 's/\.//'`
echo ">>>> FOUND $TAG : $TAG for $*"
rename "s;.chd; $TAG.chd;g" "$*" && echo ">>>> RENAMED with tag $TAG"

rm -f /tmp/binfile
rm -f /tmp/binfile.bin

exit 0
