#!/bin/sh
RP="$(realpath "$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS")"
WD="$(dirname "$RP")"

\pushd "$WD"
mv WINE WINE.keep && ln -s WINE.keep WINE
\popd
