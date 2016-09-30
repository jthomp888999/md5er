#!/usr/bin/python2.7
import hashlib, sys

file = sys.argv[1]


def op_fle(file):
	try:
		with open(file) as wd_lst:
			for word in wd_lst:
				hsh_lst(word)
	except IOError:
		print 'file not found'


def hsh_lst(word):
	word = word.rstrip('\n')
	hsh_wd = hashlib.md5(word).hexdigest()
	print "%s | %s" % (hsh_wd, word)


op_fle(file)