#!/bin/bash

pushd "$@"
${HOME}/bin/comics/magic_cbr_cbr_ext_fixer.py *.rar
${HOME}/bin/comics/magic_cbr_cbr_ext_fixer.py *.cbr
${HOME}/bin/comics/magic_cbr_cbr_ext_fixer.py *.zip
${HOME}/bin/comics/magic_cbr_cbr_ext_fixer.py *.cbz
popd
