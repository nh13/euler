#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=20

import math
import sys

n = 100
p = 1
for i in xrange(1, n+1):
    p *= i
sum = 0
p = str(p)
for i in xrange(len(p)):
    sum += int(p[i])
print "sum=%d" % sum
