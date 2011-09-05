#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=9

import math
import sys

n = 1000
a = 997
b = 2
c = 1

def is_p_trip(a, b, c):
    if (a * a) + (b * b) == (c * c):
        return True
    else:
        return False

for c in xrange(997, 3, -1):
    for b in xrange(n-c-1, 2, -1):
        a = n - c - b
        if is_p_trip(a, b, c):
            print "a=%d b=%d c=%d n=%d a*b*c=%d %s" % (a, b, c, n, (a * b * c), str(is_p_trip(a, b, c)))
            sys.exit(0)
