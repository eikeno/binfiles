#!/bin/bash

helper="${0/.sh/.lib}"


find "$(pwd)" -type f -iname "*.rar" -exec $helper {} \;
