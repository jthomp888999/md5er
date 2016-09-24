#! usr/bin/env python2.7

import hashlib, argparse, sys, time, datetime

def header():
    print """
 +-+-+-+-+-+
 |M|D|5|e|r|
 +-+-+-+-+-+
    """
# Wordlist used in testing would cause memory read errors
# open_list() function calls this function for every word

def check_hash(word):
    # stripping newlines prevents false hashes
    word = word.rstrip('\n')
    hashed = hashlib.md5(word).hexdigest()
    if (hashed == to_check):
        print "[+] Hash found %s = %s" % (to_check, word)
        # I would like to have a message that says the hash couldn't be found
        # but not repeat for every word that doesn't match

def open_list(wordlist):
    try:
        with open(wordlist) as file:
            print "[+] Checking known hashes"
            for word in file:
                # Need to setup this way to avoid MemoryError
                check_hash(word)
    except IOError:
        print "[-] File not found"
    # shouldn't be necessary after some tweaks
    # except MemoryError:
        #print "[-] File too large"

    except KeyboardInterrupt:
        print "[-] Check stopped by user"

def main():
    # Setting up command-line args (more to come)
    cli_opt = argparse.ArgumentParser(description='A simple MD5 tester.')
    cli_opt.add_argument('-m', '--md5', required=True, help='Supplies hash to be find')
    cli_opt.add_argument('-w', '--wordlist', required=True, help='Wordlist to check against')
    args = cli_opt.parse_args()

    # Defining these as global helped splitting up functions but there maybe a cleaner way?
    global to_check
    to_check = args.md5
    global wordlist
    wordlist = args.wordlist

    header()
    open_list(wordlist)


if __name__ == "__main__":
    main()