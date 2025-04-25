#/usr/bin/env python3
#! -*- coding: utf-8 -*-
"""
Rename filenames found in given directory paths with
lowercased extension.

Basename is left untouched.

"""
import os, sys, glob, shutil
from collections.abc import Callable

def usage():
	print(os.path.basename(sys.argv[0]) + ' DIR1 ... DIRn')
	sys.exit(0)

if len(sys.argv) < 2:
	print(len(sys.argv))
	print(str(sys.argv))
	usage()


CWD = os.getcwd()

for d in sys.argv[1:]:
	if not os.path.isdir(d):
		print('not a dir, skipped : ' + str(d))
		continue

	os.chdir(d)
	fl = sorted(os.listdir('.'))
	l = len(fl)
	j = 0

	for f in fl:
		bn = os.path.splitext(f)[0]
		ext =  os.path.splitext(f)[1]
		lcext = ext.lower()

		if lcext != ext:
			print('rename ' + f + ' as %s%s' % (bn, lcext))
			shutil.move(
				f,
				'%s%s' % (bn, lcext)
			)

		j += 1

	os.chdir(CWD)
