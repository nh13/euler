#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=10

import math
import sys

# Sieve of Eratosthenes
n = 2000000
s = [True for i in range(n)]
for i in range(2, int(math.sqrt(n))):
    if s[i]:
        j = i * i
        while j < n:
            s[j] = False
            j += i
sum = 0
for i in range(2, n):
    if s[i]:
        sum += i
print "sum=%d" % sum
