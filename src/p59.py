#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=59

import math
import sys

def get_char(input_text, i, key_len):
    freqs = {}
    while i < len(input_text):
        c = input_text[i]
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
        i += key_len

    max_char = 0
    max_val = 0
    s = 0
    for c in freqs:
        s += freqs[c]
        if max_val < freqs[c]:
            max_val = freqs[c]
            max_char = c
    #print "max_char=%s max_val=%d (%f)" % (max_char, max_val, max_val / float(s))
    return (max_char ^ 32)


# read in the encrypted text
fh = open("../data/p59.txt", "r")
input_text = []
for line in fh.readlines():
    line = line.rstrip("\r\n")
    for val in line.split(','):
        input_text.append(int(val))
fh.close()

# frequency analysis, knowing the space is the most frequent
key = [get_char(input_text, i, 3) for i in range(3)]
# decrypt and sum
s = 0
for i in range(len(input_text)):
    s += input_text[i] ^ key[i%3]
print(s)
