#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=48

import math
import sys

sum = 0
for i in range(1, 1001):
    sum += i ** i
x = str(sum)
print x[len(x)-10:]
