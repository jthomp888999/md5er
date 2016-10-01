#!/usr/bin/python2.7
import hashlib, sys

def OpenFile(file):
	try:
		with open(file) as wordList:
			for words in wordList:
				yield words
	except IOError:
		print '--file not found--'

def HashList(word):
    word = word.rstrip('\n')
    hashWord = hashlib.md5(word).hexdigest()
    return hashWord

def Main():
    if len(sys.argv) <= 1:
        print '--Must specify file--'
    file = sys.argv[1]
    words = OpenFile(file)

    try:
        for word in words:
            wordHash = HashList(word)
            print " %s | %s" % (wordHash, word)
    except KeyboardInterrupt:
        print '--Aborted--'

if __name__ == "__main__":
    Main()