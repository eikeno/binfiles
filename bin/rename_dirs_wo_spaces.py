#! -*- coding: utf-8 -*-

import os
import sys
import shutil
import glob

for e in os.listdir('.'):

	if not os.path.isdir(e):
		print('>> not a dir, skipped: ' + e)
		continue
	print('>>> Working on: ' + e)

	new_name = e.replace(' ', '_').replace('%20', '_')

	if os.path.exists(new_name):
		print('>>> new name already exists, skipped: ' + new_name)
		continue

	shutil.move(e, new_name)
	print('> renamed to: ' + new_name)
	print('\n')

