#!/bin/bash
# Lists gsettings ranges for all keys for each schema
# depends: gsettings

for schema in $(gsettings list-schemas | sort)
do
    for key in $(gsettings list-keys "$schema" | sort)
    do
        value="$(gsettings range "$schema $key" | tr "\n" " ")"
        echo "$schema :: $key :: $value"
    done
done

