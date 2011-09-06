#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=45

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

class square:
    def __init__(self):
        self._max = 2
        self._squares = {1 : 1, 2 : 4}

    def get_square(self, n):
        while self._max <= n:
            self._max += 1
            self._squares[self._max] = self._max * self._max
        return self._squares[n]

p = prime()
s = square()

i = 3
while True:
    # composite
    if not p.is_prime(i):
        sys.stdout.write("\r%d" % i)
        sys.stdout.flush()
        found = False
        for j in range(1, i):
            x = i - (2 * s.get_square(j))
            if x <= 0:
                break
            if p.is_prime(i-2*s.get_square(j)):
                found = True
                break
        if not found:
            print "\ni=%d" % i
            break
    i += 2 # odd only
