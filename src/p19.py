#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=19

import math
import sys

# of days in a month (no leap year)
n_a = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) 
num_days_a = sum(n_a)
# of days in a month (leap year)
n_b = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) 
num_days_b = sum(n_b)

day = 0 # 0 - Mon, ..., 6 - Sun
n = 0 # no of Sundays on the first of the month

for yr in xrange(1900, 2001):
    if 0 == (yr % 4):
        if 0 == (yr % 100):
            if 0 == (yr % 400):
                m = n_b
            else:
                m = n_a
        else:
            m = n_b
    else:
        m = n_a
    for x in m:
        if 1+day == 6 and 1901 <= yr:
            n+=1
        day += x
        day = day % 7
print "Sundays=%d" % n
