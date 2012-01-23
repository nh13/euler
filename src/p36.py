#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=36

import math
import sys
from utils import is_palindrome

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
