#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import os
import sys
import textwrap


def usage():
	print(
		textwrap.dedent("""
		USAGE:

		%s TOP_DIR

		Wilk look recursively under TOP_DIR for WEBP files and convert
		them to JPG.
		""" % (
				os.path.basename(__file__)
			)
		)
	)

def walkdir(start_path, callable):
	for p in os.listdir(start_path):
		_p = os.path.join(start_path, p)

		if os.path.islink(_p):
			sys.stderr.write('\nignoring link: %s' % str(_p))
			continue

		if os.path.isdir(_p):
			try:
				walkdir(_p, callable)
			except (OSError) as exc:
				print(str(exc))
		elif os.path.isfile(_p):
			callable(_p)
		else:
			sys.stderr.write("\nIgnoring special file: %s is" % str(_p))

def to_jpg(_f):
	_bn = os.path.basename(_f)
	_dn = os.path.dirname(_f)
	_ext = os.path.splitext(_f)[1]
	_jpg = _f.replace(_ext, '.jpg')

	if _ext.lower() != '.webp':
		return

	if os.path.exists(_jpg):
		sys.stderr.write('\n# Skipping, already exists: %s' % _jpg)
		return
	print('\n Converting to JPG: %s' % _f)
	print(os.popen("magick -quality 93 \"%s\" \"%s\"" % (_f, _jpg)).readlines())
	print()

if __name__ == '__main__':
	if len(sys.argv[:]) != 2:
		usage()
		sys.exit(1)

	if not os.path.isdir(sys.argv[1]):
		usage()
		sys.exit(2)

	walkdir(sys.argv[1], to_jpg)

