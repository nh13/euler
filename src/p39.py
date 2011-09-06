#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=39

import math
import sys

# Since a + b + c = p and a^2 + b^2 = c^2
# then c = sqrt(a^2 + b^2)
# so find a and b such that a + b + sqrt(a^2 + b^2) = p

s = {}
for a in range(1, 1001): 
    for b in range(a, 1001): 
        if a + b <= 1000:
            x = math.sqrt((a * a) + (b * b))
            c = int(x)
            p = a + b + c 
            if x == c and p <= 1000:
                if p in s:
                    s[p] += 1
                else:
                    s[p] = 1

max = 0
max_p = 0
for p in s:
    if max < s[p]:
        max = s[p]
        max_p = p
print "max=%d max_p=%d" % (max, max_p)
