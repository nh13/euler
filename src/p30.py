#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=30

import math
import sys

def check(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

def sum_pow(l, n):
    sum = 0
    for i in l:
        sum += i ** n
    return sum


def func(i, n, l, ans):
    if 0 == i: # base case
        x = sum_pow(l, n)
        if x < 10 ** len(l) and 10 ** (len(l)-1) <= x:
            y = str(x)
            a = list()
            b = list()
            for i in range(len(y)):
                a.append(int(y[i]))
                b.append(l[i])
            if check(a, b):
                ans[x] = 1
    else:
        for a in range(0, 10):
            l.append(a)
            func(i-1, n, l, ans)
            l.pop()

ans = {}
n = 5
for i in range(2, 7): # no of digits
    l = list()
    func(i, n, l, ans) 
print "nums=%s" % str(ans) 
print "ans=%d" % sum(ans.keys())
