#-*-coding: utf-8 -*-

__author__ = """ Martial Daumas - 2011-12-23 """

import os
import sys
import subprocess
import tempfile
import logging
import pdb
import traceback

from gi.repository import Gtk

SELECTED_FILE_PATHS = None
SELECTED_FILE_PATHS = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS')

OP_DIR = os.getcwd()
output_buffer = []

def cmd_run(command_line):
	_stdout = []
	_stderr = []

	# Put stderr and stdout into pipes
	proc = subprocess.Popen(command_line,
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

def do_file(filepath):

	ret, out, err = cmd_run("/usr/bin/file '%s'" % filepath)
	return out[0].decode()



if SELECTED_FILE_PATHS == None or SELECTED_FILE_PATHS == '':
	sys.exit(0)

b = Gtk.Button("ok")
w = Gtk.Window()
v = Gtk.VBox()

for filepath in SELECTED_FILE_PATHS.split('\n'):
	if filepath == '' or filepath == None:
		continue
	output_buffer.append(do_file(filepath))

for l in output_buffer:
	if len(l) > 1:
		v.pack_start(Gtk.Label(l), True, False, 3)

w.add(v)
v.pack_end(b, True, False, 10)
b.connect('clicked', Gtk.main_quit)
w.show_all()
Gtk.main()




