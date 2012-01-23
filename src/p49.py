#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=49

import math
import sys
from utils import contains_same_digits
from prime import *

p = Prime(10000)

for p1 in range(1000, 10000-(2*3330)):
    if p.is_prime(p1):
        i = 3330
        p2 = p1 + i
        p3 = p2 + i
        if p.is_prime(p2) and p.is_prime(p3) and contains_same_digits(p1, p2) and contains_same_digits(p2, p3):
            print "Found i=%d p1=%d p2=%d p3=%d %d%d%d" % (i, p1, p2, p3, p1, p2, p3)
