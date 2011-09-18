#!/usr/bin/env python

# First imported in p47

import math
import sys

class Prime:
    _primes = []
    _is_prime = []
    _max = 1

    def __init__(self):
        self._primes = list((2,3,5,7))
        self._is_prime = list((False, False, True, True, False, True, False, True))
        self._max = 7
    
    def __init__(self, max):
        self._primes = list((2,3,5,7))
        self._is_prime = list((False, False, True, True, False, True, False, True))
        self._max = 7
        self._set_max(max)

    def _set_max(self, m):
        if m < self._max or self._primes[len(self._primes)-1] == m:
            return
        prev_max = self._max
        # expand
        for i in range(prev_max, m+1):
            self._is_prime.append(True)
        prev_max = self._max
        # step through known primes
        for p in self._primes:
            x = prev_max + (p - (prev_max % p))
            if x == p:
                x += p
            while x <= m:
                self._is_prime[x] = False
                x += p
        # search for unmarked
        i = prev_max + 1
        while i * i <= m:
            if self._is_prime[i]: # unmarked
                # mark
                p = i
                x = i + p # move to 2p
                while x <= m: # 2p, 3p, 4p, ...
                    self._is_prime[x] = False
                    x += p
                i += 2 # must be odd (unless 2)
            else:
                i += 1
        # update the maximum
        self._max = m

    def is_prime(self, i):
        if self._max < i:
            self._set_max(i)
        return self._is_prime[i]

    def num_distinct_primes(self, n, max_num):
        if self.is_prime(n):
            return 1
        c = 0
        for p in self._primes:
            if n < p:
                break
            if 0 == n % p:
                c += 1
                if max_num < c:
                    return c
        if self._max < n:
            self._set_max(self._max * 2) # double it
            return self.num_distinct_primes(n, max_num)
        return c

    def get_max(self):
        return self._max

    def get_primes(self):
        i = max(self._primes) + 1
        while i <= self._max:
            if self._is_prime[i]:
                self._primes.append(i)
            i += 1
        return self._primes
