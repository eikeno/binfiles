#!/bin/bash
# Build some specific python version to be used with virtualenv
# depends : make
# depends : wget
# depends : build essentials

PHOMEDIR="$HOME/Python"

mkdir -p "$PHOMEDIR"
pushd "$PHOMEDIR" || return
wget -c 'https://www.python.org/ftp/python/3.10.16/Python-3.10.16.tgz'
wget -c 'https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tgz'
wget -c 'https://www.python.org/ftp/python/3.12.8/Python-3.12.8.tgz'
wget -c 'https://www.python.org/ftp/python/3.13.2/Python-3.13.2.tgz'

for i in ./*.tgz; do tar zxf "$i"; done
ls -1 | grep 'Python-3' | grep -v .tgz$ | while read -r py; do
	pushd "$py" || return
	./configure --prefix="${PHOMEDIR}/versions/$py" --enable-optimizations
	make install
done

mkdir -p "${HOME}/.local/bin"
for i in 2to3-3.10  idle3.10  pip3.10  pydoc3.10  python3.10; do
	cd "${HOME}/.local/bin" || exit
	rm -f "$i"
	ln -s "${PHOMEDIR}/versions/Python-3.10.16/bin/$i" .
done

for i in 2to3-3.11  idle3.11  pip3.11  pydoc3.11  python3.11; do
	cd "${HOME}/.local/bin" || exit
	rm -f "$i"
	ln -s "${PHOMEDIR}/versions/Python-3.11.11/bin/$i" .
done

for i in 2to3-3.12  idle3.12  pip3.12  pydoc3.12  python3.12; do
	cd "${HOME}/.local/bin" || exit
	rm -f "$i"
	ln -s "${PHOMEDIR}/versions/Python-3.12.8/bin/$i" .
done

for i in  idle3.13  pip3.13  pydoc3.13  python3.13; do
	cd "${HOME}/.local/bin" || exit
	rm -f "$i"
	ln -s "${PHOMEDIR}/versions/Python-3.13.2/bin/$i" .
done

cd "${PHOMEDIR}/versions" || exit
ln -s Python-3.10.16 3.10
ln -s Python-3.11.11 3.11
ln -s Python-3.12.8  3.12
ln -s Python-3.13.2  3.13

# These can now be used with custom `py' and `pyenv' wrappers

# For gi.repository support:
# pip install pygobject ; # install libgirepository1.0-dev first (debian)
