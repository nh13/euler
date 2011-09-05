#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=15

import math
import sys

n_row = 21
n_col = 21
g = [[0 for j in range(n_col)] for i in range(n_row)]
g[0][0] = 1
for i in range(n_row):
    for j in range(n_col):
        if 0 < i:
            g[i][j] += g[i-1][j]
        if 0 < j:
            g[i][j] += g[i][j-1]
print "n=%d" % g[n_row-1][n_col-1]
