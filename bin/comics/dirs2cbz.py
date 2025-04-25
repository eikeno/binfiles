#!/usr/bin/python3
# FIXME: need script global secription

import os, sys, glob, shutil
CWD = os.getcwd()

def _glob(path=None, pattern='*'):
	if not 	path:
		path = os.getcwd()

	return glob.glob(os.path.join(path, pattern))


def no_dirs_under(path=None):
	path = os.getcwd()
	_path = os.getcwd()
	if not path:
		path = os.getcwd()
	has_dirs = False

	if _path != path:
		os.chdir(path)

	for i in _glob():
		if os.path.isdir(i):
			has_dirs = True
	if _path != path:
		os.chdir(_path)

	return not has_dirs

if __name__ == '__main__':


	for d in os.listdir('.'):

		os.chdir(CWD)
		if not os.path.isdir(d):
			print('>> Selection of ' + str(d))
			print('>>> Not dir: %s, skipping ' % str(d))
			continue

		try:
			os.chdir(d)
		except:
			print("Couldn't cd to: , skipping" % str(d))
			os.chdir(CWD)
			continue

		print(">>> Entered " + str(d))
		#if no_dirs_under():
		#	print ('>> no subdirs: OK')
		print('>> has %s items' % len(_glob()))

		print(">>> Optimizing jpeg files in " + str(d))
		os.popen("jpegoptim --force -p --totals --strip-all --all-normal *.jpg").read()

		c = os.popen('zip -r "../%s.zip" *' % os.path.basename(d))
		print(c.read())

		shutil.move( '../' + os.path.basename(d) + '.zip',  '../' + os.path.basename(d) + '.cbz')

		print()

