#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=37

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

def test(n, p, l, ans):
    a = str(n)
    # 3 <= log10(n) and there is a 2,4,5,6,8 in the middle, we cannot continue
    # NB: we never introduce 4,6,8, so ignore
    if 3 <= len(a):
        if "2" in a[1:len(a)-1]:
            return
        elif "5" in a[1:len(a)-1]:
            return
    #print "on a=%s" % a
    for i in (1, 2, 3, 5, 7, 9):
        b = int(str(i) + a)
        if p.is_prime(b):
            #print "prime b=%d" % b
            test(b, p, l, ans)
    #print "a[0]=%s" % a[0]
    if a[0] in l and 1 < len(a):
        #print "On a=%s" % a
        for j in range(len(a)):
            b = int(a[:(j+1)])
            if not p.is_prime(b):
                return
        ans.append(n)

l = ("2", "3", "5", "7")
p = prime()
max = 7
ans = list()

for x in l:
    test(x, p, l, ans)
print "ans=%s sum=%d" % (str(ans), sum(ans))
