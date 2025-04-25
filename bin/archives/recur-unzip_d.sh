#!/bin/bash

helper="${0/.sh/.lib}"


find "$(pwd)" -type f -iname "*.zip" -exec $helper {} \;
