#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=36

import math
import sys

def is_palindrome(x):
    x = str(x)
    l = len(x)
    for i in range(l/2):
        if x[i] != x[l-i-1]:
            return False
    return True
    
def increment_base_two(b):
    found = False 
    for i in range(len(b)-1, -1, -1):
        if "0" == b[i]:
            b[i] = "1"
            found = True
            break
        else:
            b[i] = "0"
    if not found:
        b.insert(0, "1")
    return b

max = 1000000
sum = 0
b = ["0"]
for n in range(max):
    if is_palindrome(n) and is_palindrome(reduce(lambda x, y: str(x) + str(y), b, "")):
        sum += n
    b = increment_base_two(b)
print "sum=%d" % sum
