#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=42

import math
import sys

class Tri:
    def __init__(self):
        self._max_n = 2
        self._max = 3
        self._nums = list((1, 3))

    def is_tri(self, n):
        while self._max <= n:
            self._max_n += 1
            self._max = self._max_n * (self._max_n + 1) / 2
            self._nums.append(self._max)
        return (n in self._nums)

def word_value(word):
    sum = 0
    for i in range(len(word)):
        sum += ord(word[i]) - ord('A') + 1
    return sum

if 2 != len(sys.argv):
    sys.stderr.write("Two arguments required!\n")
    sys.exit(1)
# read in file
fn = sys.argv[1]
f = open(sys.argv[1], 'r')
line = f.readline()
f.close()
# tokenize, strip quotes, and process
tri = Tri()
n = 0
tokens = line.split(",")
for i in range(len(tokens)):
    if tri.is_tri(word_value(tokens[i][1:(len(tokens[i]))-1])):
        n += 1
print "n=%d" % n
