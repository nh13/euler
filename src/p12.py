#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=12

import math
import sys

def is_prime(primes, i):
    for p in primes:
        if 0 == (i % p):
            return False
    return True

def get_div(n, primes):
    divs = {}
    for p in primes:
        x = n
        divs[p] = 0
        while 0 == (x % p):
            divs[p] += 1
            x /= p
    return divs

def num_div(a, b, primes, to_print):
    prod = 1
    for p in primes:
        n = b[p]
        if p in a:
            n += a[p]
        if 0 < n:
            prod *= (n + 1)
            if to_print:
                print "%d : %d" % (p, n)
    return prod

# since the nth triangle number is (n * (n + 1) / 2), we can
# find the divisors of n and (n+1) separately and combine.  On
# the next loop, we are going to use (n+1), so cache it.
primes = list()
i = 3
j = 2 
l = 500
cur = {3 : 1}
while True:
    while j < i + 1:
        if is_prime(primes, j):
            primes.append(j)
        j += 1
    if 0 == ((i+1) % 2):
        next = get_div((i+1)/2, primes)
    else:
        next = get_div(i+1, primes)
    d = num_div(cur, next, primes, False) 
    n = i * (i + 1) / 2
    if l < d:
        print "i=%d n=%d d=%d" % (i, n, d)
        print "i=%d" % i
        num_div(cur, next, primes, True) 
        sys.exit(0)
    i += 1
    cur = next

# nth triangle # = n * (n + 1) / 2

# (2^2, 3^1) = 12
# 3 * 2 = 6
# 1 + 3 + 3 + 1 = 8
# 1, 2, 3, 4, 6, 12
