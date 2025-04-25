#!/usr/bin/python3
"""
Rename RAR files given as arguments to Cbr files
Case insensitive. Cbr extension if forced lower case.

"""
import os
import sys
import shutil

if __name__ == '__main__':

	if len(sys.argv) < 2:
		print(sys.argv[0] + " RAR1 ... RARn")
		sys.exit(0)

	for f in sys.argv[1:]:
		m = ''
		if f.endswith('.rar'):
			m = '.rar'
		elif f.endswith('.RAR'):
			m = '.RAR'
		else:
			print(f + "is not ending in .rar, skipped")
			continue

		shutil.move(f, f.replace(m, '.cbr'))
		print(f + ' -> ' + f.replace(m, '.cbr'))

