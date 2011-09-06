#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=40

import math
import sys

i = 0
j = 0
k = 1
p = 1
while k <= 1000000:
    i += 1
    x = str(i)
    l = len(x)
    if j <= k and k <= j + l:
        p *= int(x[k-j-1])
        k *= 10
    j += l
print "p=%d" % p
