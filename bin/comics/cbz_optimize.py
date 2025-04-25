#!/usr/bin/python3
"""
Optimize passed CBZ files using jpegoptim, for easier reading on many handheld
devices and softwares.

Accepts command line passed files as well as Nautilus selected files.

"""

import os
import logging
import tempfile
import pwd
import re
import shutil
import sys

SELECTED_FILE_PATHS = None
OP_DIR = os.getcwd()

userdir = pwd.getpwuid(os.getuid())[5]
LOGFILE = os.path.join(userdir, '.cbz_optimize.log')

logger = logging.getLogger('cbz_optimize')
hdlr = logging.FileHandler(LOGFILE)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)



def images2zip(f, d):
	'''
	@ param f Source archive filepath
	@ param d temporary directory where images are stored
	'''

	_out = re.sub('\.((c|C)(b|B)(z|Z))', '', f) + '.zip'
	out = re.sub('\.((c|C)(b|B)(z|Z))', '', f) + '.cbz'

	print('Zipping to %s...' % out)

	print(
		os.popen('7z a -r "%s" %s/*' % (_out, d)).read()
	)
	shutil.move(_out, out)

def explode(f, d):
	'''
	@param f CBZ file path
	@param d temporary directory for storing images
	'''
	print("Exploding %s under %s..." % (f, d))
	print(
		os.popen('7z e -o%s "%s"' % (d, f)).read()
	)

	print("Deleting possibly empty dirs under %s..." % d)
	print(
		os.popen('find %s -mindepth 1 -type d -exec rmdir "{}" +' % d).read()
	)

def optimize(d):
	'''
	run jpegoptim on the JPEG files under 'd'
	'''
	print("Optimizing images under %s..." % d)
	print(
		os.popen('find %s -type f -iname "*.jp*g" -exec jpegoptim --force --totals -q --all-normal --strip-all "{}" \;' % d).read()
	)

def run_all(f):
	'''
	@param f pdf file path
	'''
	d = tempfile.mkdtemp(prefix='cbz_optimize_py')
	print('Exploding %s in %s' % (f, d))
	explode(f, d)
	optimize(d)
	images2zip(f, d)
	shutil.rmtree(d)
	print('Done')

if __name__ == '__main__':

    for cbz in sys.argv[1:]:
        run_all(cbz)
