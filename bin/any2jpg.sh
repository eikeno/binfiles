#!/bin/bash
# depends: perl-rename
# depends: png2jpg_recursive.py
# depends: webp2jpg_recursive.py
# depends: avif2jpg_recursive.py
#
perl-rename "s/\.jpeg/\.jpg/" -- *.jpeg 2>/dev/null

png2jpg_recursive.py "$(pwd)"
webp2jpg_recursive.py "$(pwd)"
avif2jpg_recursive.py "$(pwd)"

rm -f -- *.png *.webp *.avif 2>/dev/null
