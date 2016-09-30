#!/usr/bin/python2.7

import hashlib, argparse, sys, time, datetime

def header():
    print """
    +-+-+-+-+-+
    |M|D|5|e|r|
    +-+-+-+-+-+
    """

# take the single md5 and the word from the list, compare them after converting words to md5's
def MatchWord(target, word):
    hashed = hashlib.md5(word).hexdigest()
    if target == hashed:
        return True

# Open the list of words, strip newlines, yield the result to be iterated over
def Openlst(wordlist):
    try:
        with open(wordlist) as file:
            for word in file:
                word = word.rstrip('\n')
                yield word
    except IOError:
        print "[-] Word-list not found"
    except KeyboardInterrupt:
        print "[-] Check stopped by user"

# creating command-line args, decide how to check hashes weather single or from file
def main():
    header()
    # Setting up command-line args (more to come)
    cli_opt = argparse.ArgumentParser(description='A simple MD5 tester.')
    cli_opt.add_argument('-m', '--md5', required=True, help='Supplies hash to be cracked')
    cli_opt.add_argument('-w', '--wordlist', required=True, help='Word-list to check against')
    args = cli_opt.parse_args()

    # Wordlist to check against
    wList = args.wordlist
    target = args.md5
    words = Openlst(wList)

    for word in words:
        test = MatchWord(target, word)
        if test == True:
            print '[+] %s | %s' % (target, word)

if __name__ == "__main__":
    main()