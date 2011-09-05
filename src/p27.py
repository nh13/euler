#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=27

import math
import sys

class prime:
    def __init__(self):
        self._primes = list((2,3))
        self._max = 3

    def _is_next_prime(self, i):
        for p in self._primes:
            if 0 == (i % p):
                return False
        return True

    def is_prime(self, i):
        while self._max <= i:
            if self._is_next_prime(self._max):
                self._primes.append(self._max)
            self._max += 1
        return (i in self._primes)

def get_len(a, b, p):
    n = 0
    while True:
        x = (n * n) + (a * n) + b
        if not p.is_prime(x):
            return n
        n += 1
        

n=1000
max = 0
max_a = max_b = 0
p = prime() 
for a in range(-n+1, n):
    sys.stdout.write("\rOn a=%d  " % a)
    sys.stdout.flush()
    for b in range(-n+1, n):
        x = get_len(a, b, p)
        if max < x:
            max = x
            max_a = a
            max_b = b
sys.stdout.write("\n")
print "max=%d max_a=%d max_b=%d" % (max, max_a, max_b)
print "coeff=%d" % (max_a * max_b)
