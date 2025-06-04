#! -*- coding: utf-8 -*-
import os
import shutil
import sys
import textwrap


def usage():
	print(
		textwrap.dedent("""
		USAGE:

		%s TOP_DIR

		Wilk look recursively under TOP_DIR files with an uppercase extension
		and will rename them with a lowercase one if possible.
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
			sys.stderr.write("\n Ignoring special file: %s is" % str(_p))

def to_lower(_f):
	_bn = os.path.basename(_f)
	_dn = os.path.dirname(_f)
	_ext = os.path.splitext(_bn)[1]
	_bn_noext = os.path.splitext(_bn)[0]
	_ext_low = str(_ext).lower()
	_f_low = os.path.join(_dn, _bn_noext + _ext_low)

	if _ext_low == _ext:
		return

	if os.path.exists(_f_low):
		sys.stderr.write('\n Skipping, already exists lowercase: %s' % _f_low)
		return

	print('\n>>> Renaming to lowercase: %s' % _f_low)
	try:
		shutil.move(_f, _f_low)
		print('OK !\n')
	except (Exception) as exc:
		print(str(exc))
		print('NOK !\n')



if __name__ == '__main__':
	if len(sys.argv[:]) != 2:
		usage()
		sys.exit(1)

	if not os.path.isdir(sys.argv[1]):
		usage()
		sys.exit(2)

	walkdir(sys.argv[1], to_lower)

