import itertools
import string

from collections import defaultdict

cipher = open("flag.cipher").read()


def xor(key, cipher):
    content = ""
    key_iter = itertools.cycle(key)
    for letter in cipher:
        k = key_iter.next()
        content += chr(ord(k) ^ ord(letter))

    return content


def valid(decrypted):
    alphabet = string.ascii_letters + string.digits + "=+/\n\r \t\"%'{}!?:"
    return all(x in alphabet for x in decrypted)


def check(position, key, cipher):
    decrypted = xor(key, cipher)
    parts = [decrypted[i:i + len(key)]
             for i in xrange(0, len(decrypted), len(key))]

    return all(valid(p[position:position + 1]) for p in parts)

key = ["\x00", "\x00", "\x00", "\x00"]
possible = defaultdict(list)
for i in xrange(len(key)):
    for c in map(chr, xrange(255)):
        key[i] = c
        if check(i, key, cipher):
            possible[i].append(c)

for f in possible[0]:
    for s in possible[1]:
        for t in possible[2]:
            for c in possible[3]:
                print xor(f + s + t + c, cipher)
