#!/usr/bin/python3
"""
Rename Zip files given as arguments to Cbz files
Case insensitive. Cbz extension if forced lower case.

"""
import os
import sys
import shutil

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print(sys.argv[0] + " ZIP1 ... ZIPn")
		sys.exit(0)

	for f in sys.argv[1:]:
		m = ''
		if f.endswith('.zip'):
			m = '.zip'
		elif f.endswith('.ZIP'):
			m = '.ZIP'
		else:
			print(f + "is not ending in .zip, skipped")
			continue

		shutil.move(f, f.replace(m, '.cbz'))
		print(f + ' -> ' + f.replace(m, '.cbz'))

