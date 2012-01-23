#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=53

import math
import sys
import string
from utils import factorial

def n_C_r(n, r, fact):
    return factorial(fact, n) / (factorial(fact, r) * factorial(fact, (n-r))) 

max = 100
count = 0
fact = {}
for n in range(1, max+1):
    for r in range(1, n): # ignores r==0, and r==n
        if 1000000 < n_C_r(n, r, fact):
            #print "n:%d r:%d" % (n, r)
            count += 1
print "count: %d" % count
