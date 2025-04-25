#-*-coding: utf-8 -*-

__author__ = """ eikeno - 2011-11-29 """

import os
import sys
import subprocess
import tempfile
import logging
import pdb
import traceback

from gi.repository import Gtk       # pylint: disable=E0611,W0611


SELECTED_FILE_PATHS = None
SELECTED_FILE_PATHS = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS')

OP_DIR = os.getcwd()


if SELECTED_FILE_PATHS == None:
	sys.exit(0)

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

def cb_destroy(widget):
	widget.destroy()
	Gtk.main_quit()

def cbr2cbz(file_path):
	_tempdir = tempfile.mkdtemp(prefix='cbr2cbz_py')
	os.chdir(_tempdir)
	ret, out, err = cmd_run('unrar x -idp "%s"' % file_path)

	file_base = os.path.splitext(os.path.basename(file_path))[0]

	zcmd = 'zip -r "' + OP_DIR + '/' + file_base + '.cbz" *'
	zret, zout, zerr = cmd_run(zcmd)

	return (zret, zout, zerr, _tempdir)

w = Gtk.Window()
v = Gtk.VBox()

for file_path in SELECTED_FILE_PATHS.split('\n'):

	if not file_path.endswith('.cbr'):
		continue

	RET, OUT, ERR, TEMPD = cbr2cbz(file_path)

	v.add(Gtk.Label(file_path))
	v.add(
		Gtk.Label(
		"# RETCODE: %s" % (str(RET))
		)
	)

	for l in ERR:
		v.add(
			Gtk.Label(
			"# STDERR: %s" % (str(l))
			)
		)

	v.add(
		Gtk.Label(
		"# Entries Count: %s" % (len(OUT))
		)
	)
	v.add(Gtk.Label("------------"))


w.add(v)
w.connect('destroy', cb_destroy)
w.show_all()

Gtk.main()
