#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=7

import math
import sys

def is_div(primes, x):
    for p in primes:
        if 0 == (x % p):
            return True
    return False

n = 10001
primes = list((2, 3, 5, 7, 11, 13))
x = 14

while n != len(primes):
    if not is_div(primes, x):
        primes.append(x)
        #print "x=%d len(primes)=%d" % (x, len(primes))
    x += 1
print "n=%d p=%d" % (n, primes[len(primes)-1])
