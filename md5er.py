#! usr/bin/env python2.7

import hashlib, argparse, sys, time, datetime

def header():
    print """
    +-+-+-+-+-+
    |M|D|5|e|r|
    +-+-+-+-+-+
    """

def Mtch_wd(toChk, word):
    hashed = hashlib.md5(word).hexdigest()
    if toChk == hashed:
        return True

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

def Op_hsh(hshFle):
    try:
        with open(hshFle) as hshLst:
            for hash in hshLst:
                hash = hash.rstrip('\n')
                yield hash
    except IOError:
        print '[-] Hash-list not found'
    except KeyboardInterrupt:
        print '[-] Check stopped by user'

def main():
    header()
    # Setting up command-line args (more to come)
    cli_opt = argparse.ArgumentParser(description='A simple MD5 tester.')
    cli_opt.add_argument('-m', '--md5', required=False, help='Supplies hash to be cracked')
    cli_opt.add_argument('-w', '--wordlist', required=True, help='Wordlist to check against')
    cli_opt.add_argument('-f', '--hashfile', required=False, help='List of md5\'s')
    args = cli_opt.parse_args()

    # Wordlist to check against
    wdLst = args.wordlist

    # If giving one single hash
    if args.md5:
        toChk = args.md5
        words = Op_lst(wdLst)
        for word in words:
           chkd = Mtch_wd(toChk, word)
           if chkd == True:
               print '[+] %s | %s' % (toChk, word)

     # If giving a file of hashes
    if args.hashfile:
        hshFle = args.hashfile
        toChk = Op_hsh(hshFle)
        words = Op_lst(wdLst)
        for chk in toChk:
            for word in words:
                chkd = Mtch_wd(chk, word)
                if chkd == True:
                    print '[+] %s | %s' % (chk, word)

if __name__ == "__main__":
    main()