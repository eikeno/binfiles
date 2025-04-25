#! -*- coding: utf-8 -*-
import os, sys, glob, shutil


def usage():
	print(os.path.basename(sys.argv[0]) + ' DIR1 ... DIRn')
	sys.exit(0)

if len(sys.argv) != 2:
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
		ext =  os.path.splitext(f)[1]
		print('%s -> %04d%s' % (f, j, ext))
		shutil.move(f, '%04d%s' % (j, ext))
		j += 1

	os.chdir(CWD)
