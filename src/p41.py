#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=41

import math
import sys

class prime:
    def __init__(self):
        self._primes = list((2,3,5,7))
        self._max = 7

    def is_prime(self, i):
        n = int(math.sqrt(i))
        while self._max <= n:
            found = False
            for p in self._primes:
                if 0 == self._max % p:
                    found = True
                    break
            if not found:
                self._primes.append(self._max)
            self._max += 1
        for p in self._primes:
            if n < p:
                return True
            elif 0 == (i % p):
                return False
        return True

def is_paradigital(n):
    x = str(n)
    d = len(x)
    for i in range(1, d+1):
        if not str(i) in x:
            return False
    return True

def test(n, d, p, max):
    nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    #print "test n=%d d=%d max=%d" % (n, d, max)
    if 0 == d:
        if max < n and p.is_prime(n):
            return n
    else:
        x = str(n)
        for i in nums[:d+len(x)]:
            if not i in x:
                max = test(int(i + x), d-1, p, max)
    return max

p = prime()
max = 0
for d in range(4, 10):
    print "On d=%d" % d
    for i in (1, 3, 7, 9):
        if i <= d:
            max = test(i, d, p, max)
print "max=%d" % max

