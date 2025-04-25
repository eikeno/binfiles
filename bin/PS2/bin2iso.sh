#!/bin/bash
# $0 BINFILE
d=$(dirname "$*")
c=$(basename "$*")
pushd "$d"

# 
echo "### $c ..."
iat "$c" > "${c/.bin/.iso}"
popd 
echo
