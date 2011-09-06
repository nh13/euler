#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=38

import math
import sys

max = 0
for i in range(1, 10000):
    x = ""
    d = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
            "6": 0, "7": 0, "8": 0, "9": 0}
    for j in range(1, 10):
        y = str(i * j)
        if "0" in y:
            break
        found = False
        for k in y:
            if d[k] == 0:
                d[k] = 1
            else:
                found = True
                break
        if found:
           break
        x = x + y
        if 9 <= len(x):
            break
    if 9 == len(x):
        m = int(x) 
        if max < m:
            max = m
print "max=%d" % max
