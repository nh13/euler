#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=52

import math
import sys
import string
from utils import contains_same_digits

def satisfies(n):
    if contains_same_digits(i, i*2) and contains_same_digits(i, i*3) and contains_same_digits(i, i*4) and contains_same_digits(i, i*5) and contains_same_digits(i, i*6):
        return True
    else: 
        return False

i = 100000
while True:
    if satisfies(i):
        print "i: %d" % i
        sys.exit(1)
    i += 1

