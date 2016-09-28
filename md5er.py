#! usr/bin/env python2.7

import hashlib, argparse, sys, time, datetime

def header():
    print """
    +-+-+-+-+-+
    |M|D|5|e|r|
    +-+-+-+-+-+
    """

# take the single md5 md5's and the word from the list, compare them after converting words to md5's
def Mtch_wd(toChk, word):
    hashed = hashlib.md5(word).hexdigest()
    if toChk == hashed:
        return True

# Open the list of words, strip newlines, yield the result to be itterated over
def Op_lst(wordlist):
    try:
        with open(wordlist) as file:
            for word in file:
                word = word.rstrip('\n')
                yield word
    except IOError:
        print "[-] Wordlist not found"
    except KeyboardInterrupt:
        print "[-] Check stopped by user"

# Open file with list of hashes, strip newlines from hashes, yield the result to be itterated over
def Op_hsh(hshFle):
    try:
        with open(hshFle) as hshLst:
            for hshLn in hshLst:
                hshLn = hshLn.rstrip('\n')
                yield hshLn
    except IOError:
        print '[-] Hash-list not found'
    except KeyboardInterrupt:
        print '[-] Check stopped by user'

# creating commandline args, decide how to check hashes weather single or from file
def main():
    header()
    # Setting up command-line args (more to come)
    cli_opt = argparse.ArgumentParser(description='A simple MD5 tester.')
    cli_opt.add_argument('-m', '--md5', required=True, help='Supplies hash to be cracked')
    cli_opt.add_argument('-w', '--wordlist', required=True, help='Wordlist to check against')
    args = cli_opt.parse_args()

    # Wordlist to check against
    wdLst = args.wordlist
    toChk = args.md5
    words = Op_lst(wdLst)

    for word in words:
        chkd = Mtch_wd(toChk, word)
        if chkd == True:
            print '[+] %s | %s' % (toChk, word)

if __name__ == "__main__":
    main()