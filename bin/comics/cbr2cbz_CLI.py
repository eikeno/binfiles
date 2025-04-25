#!/usr/bin/python3
#-*-coding: utf-8 -*-

__author__ = """ Martial Daumas - 2011-11-29 """

import os
import sys
import subprocess
import tempfile
import logging
import pdb
import shutil
import traceback

OP_DIR = os.getcwd()

logger = logging.getLogger('cbr2cbz')
hdlr = logging.FileHandler('/tmp/cbr2cbz.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def cmd_run(command_line):
	_stdout = []
	_stderr = []

	# Put stderr and stdout into pipes
	proc = subprocess.Popen(
		command_line,
		shell=True,
		stderr=subprocess.PIPE,
		stdout=subprocess.PIPE
	)

	return_code = proc.wait()

	# Read from pipes
	for line in proc.stdout:
		_stdout.append(line.rstrip())

	for line in proc.stderr:
		_stderr.append(line.rstrip())

	return (return_code, _stdout, _stderr)


def cbr2cbz(file_path):
	print('>>> cbr2cbz(%s)' % file_path)
	_tempdir = tempfile.mkdtemp(prefix='cbr2cbz_CLI_py')

	os.chdir(_tempdir)
	print('>>> CWD = %s ' % os.getcwd())
	print('>>> unrar x -idp "%s"' % file_path)
	ret, out, err = cmd_run('unrar x -idp "%s"' % file_path)

	file_base = os.path.splitext(os.path.basename(file_path))[0]
	dest_dir = os.path.dirname(file_path)

	zcmd = 'zip -r "' + dest_dir + '/' + file_base + '.cbz" *'
	zret, zout, zerr = cmd_run(zcmd)

	if str(zret) == '0':
		os.unlink(file_path)
		print('DELETED: ' + str(file_path))

	return (zret, zout, zerr, _tempdir)


if __name__ == '__main__':

	CWD = os.getcwd()

	# usage
	if len(sys.argv) == 1:
		print(sys.argv[0] + " CBR1 ... CBRn")
		sys.exit(0)

	for file_path in sys.argv[1:]:
		if not file_path.lower().endswith('.cbr'):
			print('# SKIPPED: ' + file_path + ' : bad extension')
			continue

		RET, OUT, ERR, TEMPD = cbr2cbz(os.path.join(OP_DIR, file_path))

		print(file_path)
		print("# RETCODE: %s" % (str(RET)))

		for l in ERR:
			print("# STDERR: %s" % (str(l)))

		print("# Entries Count: %s" % (len(OUT)))

		print('\n')
		os.chdir(CWD)
		shutil.rmtree(TEMPD)
