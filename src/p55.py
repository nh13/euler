#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=55

import math
import sys
import string
from utils import is_palindrome

num_iter = {}
count = 0
#for i in range(943, 944):
for i in range(1, 10000):
    n = i
    #print "On n: %d" % n
    if n in num_iter:
        if 50 <= num_iter[n]:
            count += 1
    else:
        ms = [n]
        idx = 0
        while idx <= 50:
            m = ms[idx]
            m = m + int(str(m)[::-1])
            #print "m: %d" % m
            if is_palindrome(m):
                #print "FOUND"
                for j in range(len(ms)):
                    num_iter[ms[j]] = len(ms) - j
                break
            else:
                ms.append(m)
            idx += 1
        if 50 < idx:
            count += 1
            for j in range(len(ms)):
                num_iter[ms[j]] = 51
#for n in sorted(num_iter):
#    if n < 10000:
        #print "n: %d num_iter[n]: %d" % (n, num_iter[n])
print "count: %d" % count
