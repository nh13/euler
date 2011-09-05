#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=5

import math
import sys

def add(counts, primes, n):
    for p in primes:
        c = 0
        x = n
        while 0 == (n % p):
            c += 1
            n = n / p
        if 0 < c and counts[p] < c:
            counts[p] = c

primes = (2, 3, 5, 7, 11, 13, 17, 19)
counts = {}

for p in primes:
    counts[p] = 0

for i in range(1, 20):
    add(counts, primes, i)

x = 1
for key in counts.keys():
    x *= int(math.pow(key, counts[key]))
print x
