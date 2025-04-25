#/usr/bin/env python3
#! -*- coding: utf-8 -*-

import base64
import hashlib
import os
import shutil
import sqlite3
import sys
import textwrap
import uuid

from collections.abc import Callable


_table_create_statement = """ CREATE TABLE
	comparator (
	micro_h TEXT PRIMARY KEY ASC,
	path TEXT,
	mega_h TEXT) """

_check_short_hash_statement = """ SELECT * FROM
	comparator
WHERE
	micro_h = '%s'
"""

_check_full_hash_statement = """ SELECT * FROM
	comparator
WHERE
	mega_h = '%s'
"""

_insert_short_hash_statement = """ INSERT INTO
	comparator
VALUES
	(
		"%s",
		"%s",
		"%s"
	)
"""
_delete_statement_by_short_hash = """ DELETE FROM
	comparator
WHERE
	micro_h = '%s'
"""

def usage() -> None:
	print(
		textwrap.dedent("""
		USAGE

		%s [db_asset | DB_FILE] SEARCH_DIR ON_DUPLICATED_ACTION

		Where db_asset can be: 'memory'
		DB_FILE can be an existing SQLite file, or it will be created.

		SEARCH_DIR will be scanned recusively for duplicatas.

		ON_DUPLICATED_ACTION muste be one of:
		'delete'
		'keep'
		'tagdup' -> renme duplicata with prefix: DUPLICATE_<random value>__

		""" % (
				os.path.basename(__file__)
			)
		)
	)

def walkdir(start_path: str, callable: Callable):
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

def get_md5(f: str, sample_size=None):
	if sample_size:
		try:
			return hashlib.md5(open(f, 'rb').read(sample_size)).hexdigest()
		except (IOError) as exc:
			sys.stderr.write(str(exc))
			return False
	else:
		try:
			return hashlib.md5(open(f, 'rb').read()).hexdigest()
		except (IOError) as exc:
			sys.stderr.write(str(exc))
			return False

def tagdup(f):
	return os.path.join(
		os.path.dirname(f),
		'DUPLICATE_' + uuidgen4_hex() + '__' + os.path.basename(f)
	)

def uuidgen4_hex():
	"""	Returns an uuid type '4' string	"""
	return str(uuid.uuid4()).replace('-', '')

def rename_file(_from, _to):
	try:
		shutil.move(_from, _to)
		return True
	except (EnvironmentError) as exc:
		sys.stderr.write(str(exc))
		return False

def delete_file(_file):
	try:
		os.unlink(_file)
		return True
	except (Exception) as exc:
		sys.stderr.write(str(exc))
		return False


class DBAbstract(object):
	def __init__(self):
		self.db_asset = None # Str
		self.conn = None # <sqlite3.Connection>
		self.cur = None # <sqlite3.Cursor>

	def create_table(self):
		if self.db_asset == 'memory':
			self.db_asset = ':memory:'

		try:
			if not 'comparator' in self.cur.execute(
				"SELECT * FROM sqlite_master WHERE type = 'table'"
			).fetchall()[0]:
				self.cur.execute(_table_create_statement).fetchall()
			return True
		except IndexError:
			self.cur.execute(_table_create_statement).fetchall()
			return True

	def connect(self):
		self.conn = sqlite3.connect(
			self.db_asset, # db file
			600 # timeout
		)
		self.cur = self.conn.cursor()

	def __del__(self):
		print('\nIII committing changes')
		self.conn.commit()
		print('\nIII closing connection')
		self.cur.close()

class Comparator(object):
	def __init__(self):
		self.db = None # <DBAbstract>
		self.f = None # Str (filepath)
		self.h = None # Str (md5 hexdigest)
		self.H = None # Str (md5 hexdigest)

	def inspect_file(self, f):
		print('\n# ' + str(f))
		self.f = f

		if os.path.getsize(f) < 1024*40:
			self.h = get_md5(f)
		elif os.path.getsize(f) >= 1024*40:
			self.h = get_md5(f, 1024*40)
		if not self.h:
			return

		_isindb = self.db.cur.execute(
			_check_short_hash_statement % str(self.h)
		).fetchall()

		if not _isindb:
			self.db.cur.execute(
				_insert_short_hash_statement %
					(
						self.h,
						base64.b64encode(self.f.encode()).decode(),
						'null'
					)
			).fetchall()
		else:
			self.inspect_file_deep(_isindb, f)

	def inspect_file_deep(self, check_result, new_path):

		for _recordee in check_result:
			_recordee_h = _recordee[0]
			_recordee_p = str(base64.b64decode(_recordee[1].encode()).decode())
			_recordee_H = _recordee[2]

			if new_path == _recordee_p:
				continue

			if not os.path.exists(_recordee_p):
				sys.stderr.write(
					'\nDeleting outdated record for: %s' % _recordee_p)
				self.db.cur.execute(
					_delete_statement_by_short_hash % _recordee_h
				)
				return

			if _recordee_H == 'null':
				_recordee_H = get_md5(_recordee_p)

			_new_h = _recordee_h
			_new_p =  new_path
			_new_H = get_md5(_new_p)

			if _new_H == _recordee_H:
				print ('\n%s %s' % (_new_H, _new_p))
				print('is a doublon of:')
				print('%s %s' % (_recordee_H, _recordee_p))

				if sys.argv[3] == "keep":
					print('ACTION: do nothing')

				elif sys.argv[3] == "tagdup":
					_tagged = tagdup(_new_p)
					if rename_file(_new_p, _tagged):
						print('ACTION: tag duplicate: %s' % _tagged)
					else:
						print('ACTION ABORTED: tag duplicate: %s' % _tagged)

				elif sys.argv[3] == "delete":
					if delete_file(_new_p):
						print('ACTION: deleted %s' % _new_p)
					else:
						print('ACTION ABORTED: delete: %s' % _new_p)

if __name__ == '__main__':
	if len(sys.argv[:]) != 4:
		usage()
		sys.exit(1)

	if os.path.exists('memory'):
		os.unlink('memory')

	db_abstract = DBAbstract()
	db_abstract.db_asset = sys.argv[1]
	db_abstract.connect()
	r = db_abstract.create_table()

	comparator = Comparator()
	comparator.db = db_abstract

	try:
		walkdir(sys.argv[2], comparator.inspect_file)
	except (OSError) as exc:
		print(str(exc))

