#!/usr/bin/python2.7

import hashlib
import argparse
import sys

def header():
    print """
    +-+-+-+-+-+
    |M|D|5|e|r|
    +-+-+-+-+-+
    """

# take the single md5 and the word from the list,
# compare them after converting words to md5's
def MatchWord(target, word):
    hashed = hashlib.md5(word).hexdigest()
    if target == hashed:
        return True

# Open the list of words,
# yield the result to be iterated over
def Openlst(wordlist):
    try:
        with open(wordlist) as file:
            for word in file:
                word = word.rstrip('\n')
                yield word
    except IOError:
        print "[ - ] Word-list not found"
    except KeyboardInterrupt:
        print "[ - ] Aborted"

def get_args():
    # Setting up command-line args (more to come)
    cli_opt = argparse.ArgumentParser(description='A simple MD5 matcher.')
    cli_opt.add_argument('md5', metavar='', help='Hash to check')
    cli_opt.add_argument('wordlist',metavar='' ,help='Word-list to check against')
    return cli_opt

if __name__ == "__main__":
        header()
        args = get_args()
        arg = args.parse_args()
        wList = arg.wordlist
        target = arg.md5
        words = Openlst(wList)

        for word in words:
            match = MatchWord(target, word)
            if match == True:
                print "[ + ] %s | %s\n" % (target, word)
                sys.exit()