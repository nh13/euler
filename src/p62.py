#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=62

import math
import sys


cubes = {}
digits = {}

def transform(n):
    x = sorted([str(n)[i] for i in range(len(str(n)))])
    y = ''
    for i in range(len(x)):
        y = y + x[i]
    return y 

n = 345
while True:
    c = n * n * n
    s = transform(c)
    #print "%d => %s" % (c, s)
    if not s in digits:
        digits[s] = 0
        cubes[s] = c
    digits[s] = digits[s] + 1
    if 5 <= digits[s]:
        print "Found: s=%s c=%d" % (s, cubes[s])
        break
    if 10000 < n:
        break
    n = n + 1
