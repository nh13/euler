#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=22

import math
import sys

def alpha_val(str):
    sum = 0
    for i in range(len(str)):
        sum += ord(str[i]) - ord('A') + 1
    return sum

if 2 != len(sys.argv):
    sys.stderr.write("Two arguments required!\n")
    sys.exit(1)
# read in file
fn = sys.argv[1]
f = open(sys.argv[1], 'r')
line = f.readline()
f.close()
# tokenize and strip quotes
tokens = line.split(",")
for i in range(len(tokens)):
    tokens[i] = tokens[i][1:(len(tokens[i])-1)]
# sort
tokens.sort()
# sum
sum = 0
for i in range(len(tokens)):
    sum += (i+1) * alpha_val(tokens[i])
print "sum=%d" % sum
