#! -*- coding: utf-8 -*-
# 2012-03-26

import os
import sys
import shutil

def do_prefix(prefix, _files):
	print('prefix = %s' % prefix)
	print('files = %s' % str(_files))

	for i in _files:
		print('%s' % (prefix + os.path.basename(i)))
		shutil.move(
			i,
			os.path.join(
				os.path.dirname(i),
				(prefix + os.path.basename(i))
			)
		)
	print('Done !')


if __name__ == '__main__':

	prefix = sys.argv[1]
	_files = sys.argv[2:]

	do_prefix(prefix, _files)

