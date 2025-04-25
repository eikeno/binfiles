#!/bin/bash
# $1 : path
# depends : gio

D="$(realpath "$*")"
DURL="${D/ /%20}"

echo ">>>>>>> $D"
echo ">>>>>>> $DURL"

if [[ -e "$D/icon.png" ]]; then
	gio set -t "string" "$D" "metadata::custom-icon" "file://$DURL/icon.png"
elif [[ -e "$D/.icon.png" ]]; then
	gio set -t "string" "$D" "metadata::custom-icon" "file://$DURL/.icon.png"
elif [[ -e "$D/.icon.svg" ]]; then
	gio set -t "string" "$D" "metadata::custom-icon" "file://$DURL/.icon.svg"
else
	echo ">>> No icon found for $D"
fi




