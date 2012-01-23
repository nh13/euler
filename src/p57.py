#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=57

import math
import sys

n = 1
num = 3
den = 2
count = 0

while n <= 1000:
    num += den # for the +2, NB: we already added one
    # swap
    tmp = num
    num = den
    den = tmp
    # add one denominator
    num += den
    #print "num: %d den: %d" % (num, den)
    if len(str(den)) < len(str(num)):
        #print "num: %d den: %d" % (num, den)
        count += 1
    n += 1
print "count: %d" % count
