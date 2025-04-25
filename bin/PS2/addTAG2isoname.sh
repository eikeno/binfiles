#!/bin/bash

for i in *.iso; do 
TAG=$(read-game-id.sh "$i"|cut -f2 -d:|sed -e 's/ //' -e 's/_//' -e 's/\.//')
mv "$i" "${i/.iso/ $TAG.iso}"
done

