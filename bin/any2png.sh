#!/bin/bash
for i in -- *.jpg; do convert "$i" "${i/\.jpg/\.png}"; done 
rm -f -- *.jpg

for i in -- *.webp; do convert "$i" "${i/\.webp/\.png}"; done 
rm -f -- *.webp
