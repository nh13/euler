#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=24

import math
import sys

n = 1000 
f = list((1, 1))
i = 2
while True:
    i += 1
    x = f[0] + f[1]
    if n <= len(str(x)):
        print "i=%d" % i
        break
    f[0] = f[1]
    f[1] = x
