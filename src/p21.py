#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=21

import math
import sys

def get_factors(n, primes):
    d = {1 : 1}
    for p in primes:
        x = n
        if 0 == (x % p):
            d[p] = 0
            while 0 == (x % p):
                d[p] += 1
                x /= p
    if 1 == len(d):
        primes.append(n)
    return d

def gen_divisor_sum(n, primes):
    d = get_factors(n, primes)
    divs = d.keys()
    n_factors = len(divs)
    f = [0] * n_factors # no of each factor
    out = {}
    # all combinations of factors
    while True:
        x = reduce(lambda x, y: x*y, [divs[x] ** f[x] for x in range(n_factors)], 1)
        if x < n:
            out[x] = 1
        i = 0
        while True:
            f[i] += 1
            if f[i] <= d[divs[i]]:
                break
            f[i] = 0
            i += 1
            if n_factors <= i:
                return sum(out.keys())

n = 10000
d = {1 : 1, 2 : 2}
primes = list()
primes.append(2)
for i in xrange(3, n):
    x = gen_divisor_sum(i, primes)
    d[i] = x
sum = 0
for a in xrange(1, n):
    b = d[a]
    if b < n and a < b and d[b] == a:
        sum += a + b
print "sum=%d" % sum
