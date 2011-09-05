#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=26

import math
import sys

n = 1000
m = 0
m_d = 0
for d in range(1, n):
    h = {}
    # candidate
    b = 10 ** (len(str(d))-1)
    l = 0
    s = ""
    while True:
        l += 1
        a = int((b*10) / d) # divisor
        b = (b*10) % d # remainder
        if 0 == b:
            break
        if (a, b) in h:
            # repeat!
            if m < l-h[(a,b)]:
                #print "1 / %d = 0.%s (len=%d)" % (d, s, l-h[(a,b)])
                m = l-h[(a,b)]
                m_d = d
            break
        else:
            s += str(a)
            h[(a,b)] = l
print "m=%d m_d=%d" % (m, m_d)
