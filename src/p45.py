#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=45

import math
import sys

# T: x(x+1)/2 = (x^2 + x)/2
# P: y(3y - 1)
# H: z(2z-1) = 2z^2 - z, (let z=x/2), so H: 2(x/2)^2 - x/2 = x^2/2 + x/2 = T
# So hexagonal always be triangular.  So find the next pentagonal and hexagonal:
#   want y(3y - 1) = z(2z-1)

def test_p(x):
    n = (math.sqrt((24.0*x) + 1.0) + 1.0) / 6.0
    return (n == int(n))

def test_h(x):
    n = (math.sqrt((8.0*x) + 1.0) + 1.0) / 4.0
    return (n == int(n))

def get_p(y):
    return y * ((3*y) - 1)

def get_h(z):
    return z * ((2*z) - 1)

# Lets just brute force it
z = 144
z_n = get_h(z)
while True:
    if test_p(z_n):
        print "z_n=%d" % z_n
        break
    z += 1
    z_n = get_h(z)
