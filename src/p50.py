#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=49

import math
import sys
from prime import *

max = 1000000
print "Initializing..."
p = Prime(max)
primes = p.get_primes()
max_n = 0
max_p = 0
i = len(primes)-1
prev = [primes[i] for i in range(len(primes))]
n = 1
print "Searching..."
# NB: could calculate the sums more efficiently, but this works
while True:
    next = [prev[j] for j in range(len(prev)-1)]
    found = False
    for j in range(len(next)): # add another prime
        next[j] += primes[j+n]
        if next[j] < max:
            found = True
            if p.is_prime(next[j]):
                max_n = n
                max_p = next[j]
    prev = next
    n += 1
    print "n=%d max_n=%d max_p=%d" % (n, max_n, max_p)
    if not found:
        break
print "max_n=%d max_p=%d" % (max_n, max_p)
