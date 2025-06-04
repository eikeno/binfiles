#!/usr/bin/python2.7

import sys
import pyPdf


class PdfChecker(object):

	def __init__(self, filenames_l):
		self.valid = []
		self.corrupted = {}


		for _pdf in filenames_l:
			self._check_pdf(_pdf)

		print('Valid results:')
		print(str(self.valid))

		print('Corrupted results:')
		print(str(self.corrupted))

	def _check_pdf(self, filename):
		print('Checking: %s...' % filename)
		with open(filename, 'rb') as pdf_stream:

			try:
				pyPdf.PdfFileReader(pdf_stream)#.read(pdf_stream)
				self.valid.append(filename)

			except Exception as exc:
				self.corrupted[filename] = str(exc)

		return



if __name__ == '__main__':
	print(sys.argv[1:])

	PdfChecker(sys.argv[1:])

