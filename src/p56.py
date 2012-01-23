#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=56
# HAHAH, I use python

import math
import sys
from utils import is_palindrome

def my_sum(x):
    s = str(x)
    r = 0
    for i in xrange(len(s)):
        r += int(s[i])
    return r

m = 0
for a in range(1, 101):
    for b in range(1, 101):
        cur = my_sum(a ** b)
        if m < cur:
            m = cur;
print "m: %d" % m
