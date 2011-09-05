#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=6

import math
import sys

n = 100
sum_a = ((2 * n * n * n) + (3 * n * n) + n) / 6 
sum_b = (n * n * (n + 1) * (n + 1)) / 4
print (sum_b - sum_a)
