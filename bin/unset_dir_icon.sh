#!/bin/bash
# Unset customer icon for given folder using `gio'
# depends : gio

D="$(realpath "$*")"
DURL="${D/ /%20}"

echo ">>>>>>> $D"
echo ">>>>>>>> $DURL"

gio set -t unset "$D" "metadata::custom-icon" ""





