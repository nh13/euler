#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=13

import math
import sys

d = {}
max = 0
start = -1
for i in range(1, 1000000):
    n = 0
    cur = i
    chain = list()
    chain.append(i)
    while 1 != i:
        if 0 == i % 2:
            i = i / 2
        else:
            i = (3 * i) + 1
        chain.append(i)
        if i in d:
            n = d[i]
            break
    n += len(chain)
    if max < n:
        start = cur
        max = n
    # Save results
    j = 0
    for j in range(len(chain)):
        if not chain[j] in d:
            d[chain[j]] = n - j - 1
print "max=%d start=%d" % (max, start)
