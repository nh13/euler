#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=67

import math
import sys

# generalization of p18 to handle an input file!

if 2 != len(sys.argv):
    sys.stderr.write("Two arguments required!\n")
    sys.exit(1)
# read in file
fn = sys.argv[1]
fh = open(sys.argv[1], 'r')
tri = []
for line in fh:
    line = line.rstrip("\r\n")
    tokens = line.split(" ")
    tokens = [int(tokens[i]) for i in range(len(tokens))]
    tri.append(tokens)
fh.close()

m = [[-1000000 for j in range(len(tri[len(tri)-1]))] for i in range(len(tri[len(tri)-1]))]
m[0][0] = tri[0][0]
for i in range(1, len(tri)):
    for j in range(len(tri[i])):
        m[i][j] = int(tri[i][j])

m[1][0] += m[0][0]
m[1][1] += m[0][0]
x = -1000000
for i in range(2, len(tri)):
    for j in range(len(tri[i])):
        max = m[i][j] + m[i-1][j] 
        if 0 < j and max < m[i][j] + m[i-1][j-1]:
            max = m[i][j] + m[i-1][j-1]
        m[i][j] = max
        if x < max:
            x = max
print str(m[len(m)-1])
print x
