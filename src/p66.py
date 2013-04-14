#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=66

import math
import sys

# Pell's equation!
# http://en.wikipedia.org/wiki/Pell%27s_equation
# From the section "Fundamental solution via continued fractions":
# "Thus, the fundamental solution may be found by performing the continued fraction expansion and testing each successive convergent until a solution to Pell's equation is found."
# Phew!

j = 2
val = 0
result = 0
for D in range(2, 1001):
    if D == j * j:
        j = j + 1
        continue
    m = 0
    d = 1
    a_max = int(math.floor(math.sqrt(D)))
    a = a_max

    num = a
    num_1 = 1
    den = 1
    den_1 = 0

    # find the solution
    while (num * num) - (D * den * den) != 1:
        # See p64
        m = d * a - m
        d = (D - (m * m)) / d
        a = (a_max + m) / d

        num_2 = num_1
        num_1 = num
        den_2 = den_1
        den_1 = den

        num = (a * num_1) + num_2
        den = (a * den_1) + den_2

    if val < num:
        val = num
        result = D 


print "x=%d D=%d" % (val, result)


