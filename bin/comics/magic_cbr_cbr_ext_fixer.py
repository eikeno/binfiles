#!/usr/bin/python3
"""
Use libmagic, on given RAR / ZIP files with supported extensions (ie:
.cbr, .cbz etc) to detect files with the wrong extension and fix it

"""
import os
import magic
import sys
import mimetypes
import shutil

__author__ = 'Eikeno, 2012-03-31'

TYPES = {
	b'Rar!': {
		'mimes': ['application/x-rar', 'application/rar', 'application/x-cbr'],
		'ext': ['.cbr', '.rar'] # first used for renaming
	},
	b'PK\x03\x04': {
		'mimes': ['application/zip', 'application/x-cbz'],
		'ext': ['.cbz', '.zip'] # first used for renaming
	},
	b'7z\xbc\xaf': {
		'mimes': ['application/x-7z-compressed'],
		'ext': ['.c7z', '.7z']
	}
}

def usage():
	""" print usage message and leave """
	print(os.path.basename(sys.argv[0]) + ' FILE1 ... FILEn')
	sys.exit(0)

def header_get_type(binstr):
	""" verify binary string against supported TYPES dictionnary """
	if binstr in TYPES:
		return(TYPES[binstr])
	else:
		return('None')

def change_ext(_file=None, _newext=None):
	""" Rename a file a new extension """
	if not _file:
		raise RuntimeError('_file cannot be None')
	if not _newext:
		raise RuntimeError('_newext cannot be None')

	_base = os.path.splitext(_file)[0]
	_newname = _base + _newext
	shutil.move(_file, _newname)
	print('Done !')

def check_and_fix(files_l):
	"""
	Check files from 'files_l' list. If they have an extension not conform
	to what's expected, fix it

	 """

	for _file in files_l:

		_ext = os.path.splitext(_file)[1]
		print('>>> ' + _file)

		with open(_file, 'rb') as _f:
			binstr = _f.read(4)
			_real = header_get_type(binstr)

		if not _real:
			print('Unsupported type - skip')
			continue

		try:
			real_mimes = _real['mimes']
		except TypeError:
			continue

		real_ext = os.path.splitext(_file)[0]
		if not real_ext or real_ext == '':
			real_ext = None

		guessed_mime = mimetypes.guess_type(_file)[0]

		if guessed_mime not in real_mimes:
			print('%s is type:\n%s\n but has an extension of type:\n%s' % (
				_file,
				str(real_mimes),
				str(guessed_mime)
				)
			)
			print('Renaming using: %s extension' % _real['ext'][0])
			change_ext(_file, _real['ext'][0])

		# supported type, try to use prefered extension:
		elif real_ext:
			if real_ext != _real['ext'][0]:
				print('Renaming using: %s extension' % _real['ext'][0])
				change_ext(_file, _real['ext'][0])
		else:
			print('OK')

		print()

if __name__ == '__main__':
	CWD = os.getcwd()

	if len(sys.argv) < 2:
		print(str(sys.argv))
		usage()

	_files = sys.argv[1:]

	check_and_fix(_files)
