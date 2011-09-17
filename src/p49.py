#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=49

import math
import sys
from prime import *

def contains_same_digits(a, b, c):
    a = str(a)
    b = str(b)
    c = str(c)
    for i in range(len(a)):
        found = False
        for j in range(len(b)):
            if a[i] == b[j]:
                b = b[0:j] + 'X' + b[j+1:len(b)]
                found = True
                break
        if not found:
            return found
        found = False
        for j in range(len(c)):
            if a[i] == c[j]:
                c = c[0:j] + 'X' + c[j+1:len(c)]
                found = True
                break
        if not found:
            return found
    return True

p = Prime(10000)

for p1 in range(1000, 10000-(2*3330)):
    if p.is_prime(p1):
        i = 3330
        p2 = p1 + i
        p3 = p2 + i
        if p.is_prime(p2) and p.is_prime(p3) and contains_same_digits(p1, p2, p3):
            print "Found i=%d p1=%d p2=%d p3=%d %d%d%d" % (i, p1, p2, p3, p1, p2, p3)
