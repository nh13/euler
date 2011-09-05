#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=29

import math
import sys

t = {}
n = 100
for a in range(2, n+1):
    for b in range(2, n+1):
        x = a ** b
        t[x] = 1
print len(t)        
