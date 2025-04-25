#!/usr/bin/python3

import os, shutil, sys, glob, subprocess

RDIR = os.getcwd()

for d in glob.glob('*'):
	if os.path.isdir(d):
		print(" ++ " + d)
		try:
			os.chdir(d)
		except:
			sys.exit(1)

		sys.stderr.write('jpegoptim --force -t -v --strip-all *.jpg -> ')
		_cmd = 'jpegoptim --force -t -v --strip-all *.jpg'
		return_code = subprocess.call(_cmd, shell=True)
		if return_code != 0:
			sys.exit(10)
		sys.stderr.write(str(return_code) + '\n')
		print('\n')

		sys.stderr.write("Creating %s.cbz -> " % os.path.basename(d))
		_cmd = "zip -r '../%s.zip' *.jpg" % os.path.basename(d)
		return_code = subprocess.call(_cmd, shell=True)
		if return_code != 0:
			sys.exit(20)
		sys.stderr.write(str(return_code) + '\n')

		try:
			os.chdir(RDIR)
		except:
			sys.exit(1)

		print("Done !")
		print('\n')
