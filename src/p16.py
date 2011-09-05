#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=16

import math
import sys

x = str(int(math.pow(2, 1000)))
sum = 0
for j in range(len(x)):
    sum += int(x[j])
print "sum=%d" % sum
