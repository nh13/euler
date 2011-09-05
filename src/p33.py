#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=33

import math
import sys

def is_prime(primes, i):
    for p in primes:
        if 0 == (i % p):
            return False
    return True

def check(n, d, a, b):
    if 0 < a and 0 < b:
        return (n / float(d) == a / float(b))
    else:
        return False

# generate primes
primes = list((2,3))
for i in range(5, 100):
    if is_prime(primes, i):
        primes.append(i)

# find candidates
t = list()
for n in range(10, 100):
    x = str(n)
    for d in range(n+1, 100):
        y = str(d)
        if x[0] == y[0] and check(n, d, int(x[1]), int(y[1])):
            t.append(list((n, d)))
        elif x[0] == y[1] and not "0" == y[1] and check(n, d, int(x[1]), int(y[0])):
            t.append(list((n, d)))
        elif x[1] == y[0] and not "0" == x[1] and check(n, d, int(x[0]), int(y[1])):
            t.append(list((n, d)))
        elif x[1] == y[1] and not "0" == x[1] and not "0" == y[1] and check(n, d, int(x[0]), int(y[0])):
            t.append(list((n, d)))

# multiply 
n = 1
d = 1
for x in t:
    n *= x[0]
    d *= x[1]

# reduce
for p in primes:
    while 0 == n % p and 0 == d % p:
        n /= p
        d /= p
print "n=%d d=%d" % (n, d)
