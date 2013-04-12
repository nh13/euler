#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=63

import math
import sys

n = 0
for b in range(1, 10): # no need to go above base as 10
    e = 1 
    while True:
        v = b ** e
        l = len(str(v)) 
        if l == e:
            n = n + 1
        elif l < e: # here's the crux
            break
        e = e + 1
print "Ans=%d" % n
