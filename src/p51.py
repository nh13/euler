#!/usr/bin/env python
# requires python 2.6 or greater

# http://projecteuler.net/index.php?section=problems&id=51

import math
import sys
import string
import itertools
from prime import *

def findsubsets(S):
    s = set()
    for i in range(2, len(S)+1):
        #print "i=%d\t%s" % (i, str(set(itertools.combinations(S, i))))
        s = s.union(set(itertools.combinations(S, i)))
    return s

def is_p51(n, fam, p):
    x = 10 - fam + 1
    # ex. for 8, only change 0,1,2
    s = str(n)
    d = {}
    for i in range(len(s)):
        y = int(s[i])
        if y <= x:
            if not y in d:
                d[y] = [i]
            else:
                d[y].append(i)
    for j in d.keys():
        #print "Starting testing key=%d d[j]=%s" % (j, str(d[j]))
        for subset in findsubsets(d[j]):
            #print "Testing subset=%s" % str(subset)
            n_false = 10 - j - fam # the number we can find to be false 
            count = 1
            mylist = [n]
            #print "n_false=%d" % n_false
            for k in range(j+1, 10): 
                t = [s[l] for l in range(len(s))]
                t = ''
                for l in range(len(s)):
                    if l in subset:
                        t += str(k)
                    else:
                        t += str(s[l])
                num = int(t)
                #print "Testing num=%d" % num
                if not p.is_prime(num):
                    #print "Not prime"
                    n_false -= 1
                    if n_false < 0:
                        break # new subset
                else:
                    #print "num is prime: %d" % num
                    count += 1
                    mylist.append(num)
                    if fam <= count:
                        print "list: %s" % str(mylist)
                        for z in mylist:
                            print "z=%d prime=%s" % (z, str(p.is_prime(z)))
                        return True
    return False


#fam = 7
fam = 8
p = Prime(100000)
i = 10000

while True:
    if p.is_prime(i):
        #print "Testing p=%d" % i
        if is_p51(i, fam, p):
            print "Found i=%d" % i
            sys.exit(1)
    i += 1
