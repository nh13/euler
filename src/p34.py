#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=34

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

def check(n, fact):
    sum = 0
    for x in str(n):
        sum += factorial(fact, int(x))
    return (n == sum)

fact = {0 : 1, 1 : 1}

# get a horrible maximum value
max = 1
while True:
    x = int('9' * max) 
    print "a=%d b=%d" % (max * factorial(fact, 9), 10 ** max)
    if max * factorial(fact, 9) < 10 ** max:
        break
    max += 1
max = max * factorial(fact, 9)
print "max=%d" % max

# brute force
sum = 0
i = 3
while i < max:
    if check(i, fact):
        sum += i
        print "i=%d sum=%d" % (i, sum)
    i += 1
