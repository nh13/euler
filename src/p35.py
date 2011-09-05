#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=35

import math
import sys

# NB: assumes primes is in sorted order
def is_prime(primes, i):
    s = int(math.sqrt(i))
    for p in primes:
        if s < p:
            return True
        if 0 == (i % p):
            return False
    return True

def check(n, primes):
    x = str(n)
    if 1 == len(x):
        return True
    for l in ("0", "2", "4", "5", "6", "8"):
        if l in x:
            return False
    # rotate
    a = x
    for i in range(1, len(x)):
        a = a[1:] + a[0]
        if not int(a) in primes:
            return False
    return True

# generate primes
primes = list((2,3))
for i in range(5, 1000000):
    if is_prime(primes, i):
        primes.append(i)

#print "primes=%s" % str(primes)
count = 0
for p in primes:
    if check(p, primes):
        count += 1
        print "p=%d" % p
print "count=%d" % count
