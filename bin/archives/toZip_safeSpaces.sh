#!/bin/bash
unset name
name=$(basename "$*" )
pushd "$*" &&
zip "$name".zip * &&
popd
