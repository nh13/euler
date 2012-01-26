#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=58

import math
import sys
from prime import *

def get_diag(n):
    if 1 == n:
        return 1
    br = ((n-2) * (n-2)) + (n-1)
    bl = br + n-1
    tl = bl + n-1
    tr = tl + n-1
    return [tr, tl, bl, br]

p = Prime(100000)

br = 1
n = 3
k = 50
prime = 0
total = 1.0
while True:
    tr = br + n-1
    tl = tr + n-1
    bl = tl + n-1
    br = bl + n-1
    total += 4
    if p.miller_rabin(tr, k):
        prime += 1
    if p.miller_rabin(tl, k):
        prime += 1
    if p.miller_rabin(bl, k):
        prime += 1
    # NB: bottom right will always be a square number
    #print "n=%d prime: %d total: %d frac: %f" % (n, prime, total, prime / total)
    if prime / total < 0.1:
        print "n: %d" % n
        break
    n += 2
