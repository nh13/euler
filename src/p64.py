#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=64

import math
import sys

# From: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
# m_0 = 0
# d_0 = 1
# a_0 = \floor{\sqrt{S}}
# m_{n+1} = d_n a_n - m_n
# d_{n+1} = \frac{S - m^2_{n+1}}{d_n}
# a_{n+1} = \floor{\frac{\floor{S} + m_{n+1}}{d_{n+1}}} = \floor{\frac{a_0 + m_{n+1}}{d_{n+1}}}

def get_key(m, d, a):
    return str(m) + ":" + str(d) + ":" + str(a)

def get_period(S):
    m = [0]
    d = [1]
    a = [int(math.floor(math.sqrt(S)))]
    values = {get_key(m, d, a) : True}
    #print "m=%d d=%d a=%d" % (m[0], d[0], a[0])

    i = 0
    while True:
        m_n = d[i] * a[i] - m[i] 
        d_n = (S - (m_n * m_n)) / d[i]
        a_n = int(math.floor((a[0] + m_n) / d_n))
        #print "m=%d d=%d a=%d" % (m_n, d_n, a_n)
        s = get_key(m_n, d_n, a_n)
        if s in values:
            #print "Found: S=%d i=%d a=%s" % (S, i, str(a[1:]))
            return i
        values[s] = True
        m.append(m_n)
        d.append(d_n)
        a.append(a_n)
        i = i + 1

j = 2
n = 0
for i in range(2, 10000+1):
    if i == j*j:
        j = j + 1
        continue
    p = get_period(i)
    if 1 == (p % 2):
        n = n + 1
print "Ans: %d" % n
