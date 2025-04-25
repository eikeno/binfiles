#! -*- coding: utf-8 -*-

import glob
import os
import shutil

def make_folder_with_parents(folder):
	"""
	Create folder with its parent parts if not existing

	"""

	try:
		os.makedirs(folder)

	except (OSError) as exc:
		pass



_all = os.listdir('.')

for _item in _all:

	_item_type = '-'
	if os.path.isdir(_item):
		_item_type = 'D'

	_item_ext = '-'

	if _item_type == '-':
		_item_bn = None
		_item_bn, _item_ext = os.path.splitext(_item)

	else:
		_item_bn = os.path.basename(_item)
		_item_ext = '---'

	print('%s\t%s\t%s' % (_item_type, _item_ext, _item_bn))


	if _item_type == '-':
		make_folder_with_parents(_item_bn)
		shutil.move(_item, _item_bn)
