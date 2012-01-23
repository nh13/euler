#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=4

import math
import sys
from utils import is_palindrome

m = -1
m_a = -1
m_b = -1
for a in xrange(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if is_palindrome(x):
            if m < x:
                m = x
                m_a = a
                m_b = b
print "m=%d m_a=%d m_b=%d" % (m, m_a, m_b)
