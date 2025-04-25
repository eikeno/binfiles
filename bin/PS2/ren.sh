#!/bin/bash

echo "== $1 ==="
d=`dirname "$1"`
b=$(basename "$d")
#echo "b = $b"
mv "$1" "$d/$b.iso"
echo 
exit 0
