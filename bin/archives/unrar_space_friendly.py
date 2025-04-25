#!/usr/bin/python

import os, sys, glob, shutil
CWD = os.getcwd()

#if len(sys.argv) < 2:
#	print(sys.argv[0] + ' CBR1 ... CRBn')
#	sys.exit(0)

print("############# RAR")

for c in glob.glob('*.rar'):
	if not os.path.isfile(c):
		print('not a file, skipping: ' + str(c))
		continue

	print('>>> %s' % str(c))
	os.makedirs(os.path.splitext(c)[0])
	os.chdir(os.path.splitext(c)[0])
	for l in os.popen('unrar x -idp "../%s"' % c).readlines():
		print(l + '\n')
	os.chdir(CWD)

print("############# CBR")
for c in glob.glob('*.cbr'):
	if not os.path.isfile(c):
		print('not a file, skipping: ' + str(c))
		continue

	print('>>> %s' % str(c))
	os.makedirs(os.path.splitext(c)[0])
	os.chdir(os.path.splitext(c)[0])
	for l in os.popen('unrar x -idp "../%s"' % c).readlines():
		print(l + '\n')
	os.chdir(CWD)
