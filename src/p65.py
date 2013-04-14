#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=65

import math
import sys

d = 1
n = 2

# Observation:
#n_k = a_{k-1} * n_{k-1} + n_{k-2} 
#n_1 = 2
#n_2 = 3
#n_3 = 2 * 3 + 2 = 8
#n_4 = 1 * 8 + 3 = 11
#n_5 = 1 * 11 + 8 = 19
#n_6 = 4 * 19 + 11 = 87
#n_7 = 1 * 87 + 19 = 106
#n_8 = 1 * 106 + 87 = 193
#n_9 = 6 * 193 + 106 = 1264
#n_10 = 1 * 1264 + 193 = 1457

for i in range(2, 101):
    x = d
    c = 1
    if 0 == i % 3:
        c = 2 * int(i / 3)
    d = n
    n = c * d + x
    #print n
s = str(n)
r = 0
for i in range(len(s)):
    r = r + int(s[i])
print "Ans: %d" % r
