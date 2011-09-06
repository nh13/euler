#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=44

import math
import sys

def test_p(x):
    n = (math.sqrt((24.0*x) + 1.0) + 1.0) / 6.0
    return (n == int(n))

# Brute force, to the rescue
D = 10000000000000
i = 2
l = list()
while True:
    if test_p(i):
        # Note the difference between the next lowest is 3i - 2
        if D < (3*i) - 2:
            break
        l.insert(0, i) # cache
        for j in l: 
            if test_p(i-j) and test_p(i+j):
                if i - j < D:
                    D = i - j
    i += 1
print "\nD=%d" % D
