#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=28

import math
import sys

def sum_diag(n):
    if 1 == n:
        return 1
    br = ((n-2) * (n-2)) + (n-1) 
    bl = br + n-1
    tl = bl + n-1
    tr = tl + n-1
    return br + bl + tl + tr + sum_diag(n-2)


n = 1001
print "i=%d sum_diag=%d" % (n, sum_diag(n))
