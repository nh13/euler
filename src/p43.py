#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=43

import math
import sys

# NB: we could cache this...
# for 7 use x=7, y=-2
# for 11 use x=11, y=-1
# for 13 use x=13, y=4
# for 17 use x=17, y=-5
def div_x(d1, d2, x, y):
    l = list()
    # want all d3 such that 0 == ((d1*d10) + d2 - y*d3) % x
    n = (d1*10) + d2
    i = 0 # additional sum required
    j = 0 # d3 minimum 
    while 0 != (n+i) % x and j < 10:
        i += y 
        j += 1
    if 10 == j:
        return l
    for i in xrange(j, 10, x):
        l.append(i)
    return l

sum = 0

d = {}
for i in range(10):
    d[i] = 0
for d1 in range(1, 10):
    d[d1] = 1
    for d2 in range(10):
        if d[d2] == 1:
            continue
        d[d2] = 1
        for d3 in range(10):
            if d[d3] == 1:
                continue
            d[d3] = 1
            # since d4 must be divisible by 2 or be zero
            for d4 in (0, 2, 4, 6, 8):
                if d[d4] == 1:
                    continue
                d[d4] = 1
                # since for something to be divisible by 3, the
                # sum of its digits must be divisible by 3
                start_d5 = (3 - ((d3 + d4) % 3)) % 3
                for d5 in range(start_d5, 10, 3):
                    if d[d5] == 1:
                        continue
                    d[d5] = 1
                    # since d4d5d6 must be divisible by 5
                    for d6 in (0, 5):
                        if d[d6] == 1:
                            continue
                        d[d6] = 1
                        for d7 in div_x(d5, d6, 7, -2): # 7
                            if d[d7] == 1:
                                continue
                            d[d7] = 1
                            for d8 in div_x(d6, d7, 11, -1): # 11
                                if d[d8] == 1:
                                    continue
                                d[d8] = 1
                                for d9 in div_x(d7, d8, 13, 4): # 13
                                    if d[d9] == 1:
                                        continue
                                    d[d9] = 1
                                    for d10 in div_x(d8, d9, 17, -5): # 17
                                        if d[d10] == 1:
                                            continue
                                        x = "%d%d%d%d%d%d%d%d%d%d" % (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
                                        #print "x=%s" % x
                                        sum += int(x)
                                    d[d9] = 0
                                d[d8] = 0
                            d[d7] = 0
                        d[d6] = 0
                    d[d5] = 0
                d[d4] = 0
            d[d3] = 0
        d[d2] = 0
    d[d1] = 0
print "sum=%d" % sum
