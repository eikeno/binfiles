#!/usr/bin/python3
"""
Covert passed PDF files to CBZ files, for easier reading on many handheld
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
SELECTED_FILE_PATHS = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS')
OP_DIR = os.getcwd()

userdir = pwd.getpwuid(os.getuid())[5]
LOGFILE = os.path.join(userdir, '.pdf2images.log')

logger = logging.getLogger('pdf2cbz')
hdlr = logging.FileHandler(LOGFILE)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)



def images2zip(f, d):
	'''
	@ param d temporary directory where images are stored
	'''
	_out = re.sub('\.((p|P)(d|D)(f|F))', '', f) + '.zip'
	out = re.sub('\.((p|P)(d|D)(f|F))', '', f) + '.cbz'

	print('Zipping to %s...' % out)

	print(
		os.popen('7z a "%s" %s/*.jpg' % (_out, d)).read()
	)
	shutil.move(_out, out)

def explode(f, d):
	'''
	@param f pdf file path
	@param d temporary directory for storing images
	'''
	_prefix = os.path.basename(f)
	_prefix = re.sub('\.((p|P)(d|D)(f|F))', '', _prefix)
	_root = os.path.join(d, _prefix)
	print("Running pdfimages under %s..." % d)
	print(
		os.popen('pdfimages -j "%s" "%s"' % (f, _root)).read()
	)

def optimize(d):
	'''
	run jpegoptim on the JPEG files under 'd'
	'''
	print("Optimizing images under %s..." % d)
	print(
		os.popen('jpegoptim -f -t -v --strip-all %s/*.jpg' % d).read()
	)

def pdf2cbz(f):
	'''
	@param f pdf file path
	'''
	d = tempfile.mkdtemp(prefix='pdf2cbz_py')
	print('DEBUG: exploding in %s' % d)
	explode(f, d)
	optimize(d)
	images2zip(f, d)
	shutil.rmtree(d)
	print('Done')

def pdf2cbz_if_possible(f):
	'''
	check if f is really a pdf file. If yes, pass it to pdf2cbz()
	'''
	# __CODEME__
	pdf2cbz(f)

if __name__ == '__main__':

	# _tempdir = tempfile.mkdtemp(prefix='cbr2cbz_CLI_py')
	if SELECTED_FILE_PATHS:
		for pdf in SELECTED_FILE_PATHS:
			pdf2cbz(pdf)
	else:
		for pdf in sys.argv[1:]:
			pdf2cbz_if_possible(pdf)
