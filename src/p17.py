#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=17

import math
import sys

# digits: one, two, three, ...
a_s = {0 : "zero", 1 : "one", 2 : "two", 3 : "three",
        4 : "four", 5 : "five", 6 : "six", 7 : "seven",
        8 : "eight", 9 : "nine"}
# 0-19
b_s = {0 : "zero", 1 : "one", 2 : "two", 3 : "three",
        4 : "four", 5 : "five", 6 : "six", 7 : "seven",
        8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven",
        12 : "twelve", 13 : "thirteen", 14 : "fourteen",
        15 : "fifteen", 16 : "sixteen", 17 : "seventeen",
        18 : "eighteen", 19 : "nineteen"}
# twenty-ninety: 
c_s = {2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty",
        6 : "sixty", 7 : "seventy", 8 : "eighty", 9 : "ninety"}

# dictionaries
a = {}
for i in range(10):
    a[i] = len(a_s[i])
b = {}
for i in range(20):
    b[i] = len(b_s[i])
c = {}
for i in range(2, 10):
    c[i] = len(c_s[i])

def get_l(i):
    x = str(i)
    n = 0
    if 1000 <= i:
        n += 8 # thousand
        i = i % 1000
        n += a[int(x[0])]
        x = x[1:]
    if 100 <= i:
        n += 7 # hundred
        i = i % 100
        n += a[int(x[0])]
        x = x[1:]
        if 0 < i:
            n += 3 # and
    if 0 < i:
        if i < 20:
            n += b[i]
        else:
            n += c[int(i/10)]
            i = i % 10
            if 0 < i:
                n += b[i]
    return n

sum = 0;
for i in range(1, 1001):
    #print "i=%d l=%d" % (i, get_l(i))
    sum += get_l(i)
print "sum=%d" % sum

