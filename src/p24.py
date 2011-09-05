#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=24

import math
import sys

def factorial(fact, n):
    if not n in fact:
        x = 1
        y = 1
        while x <= n:
            y *= x
            if not x in fact:
                fact[x] = y
            x += 1
    return fact[n]

def get_nth(digits, n, fact):
    # base case
    if 1 == len(digits):
        if 1 < n:
            sys.stderr.write("Error!\n")
            sys.exit(1)
        return str(digits[0])
    m = factorial(fact, len(digits)-1)
    x = digits[n/m]
    l = list()
    for d in digits:
        if d != x:
            l.append(d)
    return str(x) + get_nth(l, n % m, fact)


fact = {1 : 1}
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
n = 1000000 - 1 # zero-based
print "n=%d digits=%s nth=%s" % (n, str(digits), str(get_nth(digits, n, fact)))
