#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=3

import math

def is_prime(x):
    for i in xrange(2, int(math.sqrt(x)) + 1):
        # ignore even numbers not 2
        if 2 == i or (2 < i and 0 != i % 2):
            if 0 == (x % i):
                return False
    return True

def get_max_prime_div(val):
    for i in xrange(int(math.sqrt(val)), 1, -1):
        if 0 == (val % i) and is_prime(i):
            return i
    return 0

print "2=%s" % str(is_prime(2))
print "3=%s" % str(is_prime(3))
print "4=%s" % str(is_prime(4))
print "600851475143=%s" % str(is_prime(600851475143))

print "2=%d" % get_max_prime_div(2)
print "3=%d" % get_max_prime_div(3)
print "4=%d" % get_max_prime_div(4)
print "600851475143=%d" % get_max_prime_div(600851475143)
