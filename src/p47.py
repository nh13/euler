#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=47

import math
import sys
from prime import * 

# could use a sieve, but brute force works too
n = 4
p = Prime(1000)
i = 2 * 3 * 5 * 7
a = p.num_distinct_primes(i, n)
while True:
    print "1 i=%d" % i
    while n != a:
        i += 1
        a = p.num_distinct_primes(i, n)
    found = True
    for j in xrange(1, n):
        b = p.num_distinct_primes(i+1, n)
        #print "HERE i=%d a=%s b=%s" % (i, a, b)
        if n != b:
            i += 1
            a = b
            found = False
            break
        else:
            i += 1
            a = b
    if found:
        print "i=%d" % (i-n+1)
        break
