#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=32

import math
import sys
import copy

def get_dict(n, d):
    x = str(n)
    for i in range(len(x)):
        if "0" == x[i]:
            return False
        elif x[i] in d:
            return False
        else:
            d[x[i]] = 1
    return True

# NB: valid dim:
# 1 X 4 = 4
# 2 X 3 = 4

# no of digits #1
sum = 0
prods = list()
for i in range(1, 3):
    j = 5 - i # no of digits #2
    # range #1
    for k in range(10 ** (i-1), 10 ** i):
        d = {}
        if get_dict(k, d):
            for l in range(10 ** (j-1), 10 ** j):
                p = k * l
                if not p in prods and 10 ** 3 <= p and p < 10 ** 4: 
                    e = copy.deepcopy(d) 
                    if get_dict(l, e):
                        if get_dict(p, e):
                            sum += p
                            prods.append(p)
                            print "k=%d l=%d p=%d" % (k, l, p)
print "sum=%d" % sum
