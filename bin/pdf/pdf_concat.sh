#!/bin/sh

gs -q -sPAPERSIZE=letter -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=../output.pdf $*
ls -alh ../output.pdf
