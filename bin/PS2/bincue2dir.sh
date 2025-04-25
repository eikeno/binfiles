#!/bin/bash
# $1 : none
# prend les fichier "foo.bin" et "foo.cue" et les place
# dans un dossier "foo"

for i in *.cue; do
  BN="${i/.cue/}"
  echo $i
  echo $BN
  mkdir -p "$BN"
  mv "$i" "$BN"
  mv "${i/.cue/.bin}" "$BN"
done
