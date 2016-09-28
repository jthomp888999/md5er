#!/usr/bin/env python2.7

def Op_hsh(hshFle):
    try:
        with open(hshFle) as file:
            for hashes in file:
                hashes = hashes.rstrip('\n')
                yield hashes
    except IOError:
        print '[-] Hash-list not found'
    except KeyboardInterrupt:
        print '[-] Check stopped by user'


a = Op_hsh('hashlist.txt')
for b in a:
    print(b)