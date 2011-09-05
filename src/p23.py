#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=23

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

n = 28123
# find the abundant #s
primes = list()
primes.append(2)
ab = list()
for i in xrange(3, n+1):
    x = gen_divisor_sum(i, primes)
    if i < x:
        ab.append(i)
        #print "i=%d x=%d" % (i, x)
print "found %d abundant #s" % len(ab)
# find all sums of abundant #s 
s = {}
for i in xrange(len(ab)):
    for j in xrange(i, len(ab)):
        x = ab[i] + ab[j]
        if x <= n:
            s[x] = 1
print "found %d sums" % len(s)
# go through
sum = 0
for i in xrange(n+1):
    if not i in s:
        sum += i
print "sum=%d" % sum
