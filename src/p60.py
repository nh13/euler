#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=60

import math
import sys
import copy
from prime import *

# TODO: we need a much faster solution for this...

def check_adj(adj, i, p_list):
    if 0 < len(adj[i]) and -1 == adj[i][0]:
        print "Building adjacency for %d (%d) (%d)" % (i, p_list[i], len(p_list))
        adj[i] = []
        for j in xrange(i+1, len(p_list)):
            #if p.is_prime(int(str(p_list[i]) + str(p_list[j]))) and p.is_prime(int(str(p_list[j]) + str(p_list[i]))):
            if p.miller_rabin(int(str(p_list[i]) + str(p_list[j])), 50) and p.miller_rabin(int(str(p_list[j]) + str(p_list[i])), 50):
                adj[i].append(j)
                #adj[j].append(i)

n = 20000
while True:
    print "Building primes..."
    p = Prime(n)
    p_list = copy.deepcopy(p.get_primes())

    # NB: could re-use previous
    adj = [[-1] for i in xrange(len(p_list))]

    print "Iterating..."
    mysum = 0
    best_sum = 1000000
    for a in xrange(len(p_list)):
        if best_sum < a * 5:
            break
        #print "[%d]" % (p_list[a])
        mysum += p_list[a]
        check_adj(adj, a, p_list)
        for b in xrange(a+1, len(p_list)):
            if best_sum < mysum + p_list[b] * 4:
                break
            if b not in adj[a]:
                continue
            #print "[%d, %d]" % (p_list[a], p_list[b])
            mysum += p_list[b]
            check_adj(adj, b, p_list)
            for c in xrange(b+1, len(p_list)):
                if best_sum < mysum + p_list[c] * 3:
                    break
                if c not in adj[b] or c not in adj[a]:
                    continue
                #print "[%d, %d, %d]" % (p_list[a], p_list[b], p_list[c])
                mysum += p_list[c]
                check_adj(adj, c, p_list)
                for d in xrange(c+1, len(p_list)):
                    if best_sum < mysum + p_list[d] * 2:
                        break
                    if d not in adj[c] or d not in adj[b] or d not in adj[a]:
                        continue
                    print "[%d, %d, %d, %d]" % (p_list[a], p_list[b], p_list[c], p_list[d])
                    mysum += p_list[d]
                    check_adj(adj, d, p_list)
                    for e in xrange(d+1, len(p_list)):
                        if best_sum < mysum + p_list[e]:
                            break
                        if e not in adj[d] or e not in adj[c] or e not in adj[b] or e not in adj[a]:
                            continue
                        print "[%d, %d, %d, %d, %d]" % (p_list[a], p_list[b], p_list[c], p_list[d], p_list[e])
                        if mysum + p_list[e] < best_sum:
                            best_sum = mysum + p_list[e]
                            print "Found [%d, %d, %d, %d, %d]" % (p_list[a], p_list[b], p_list[c], p_list[d], p_list[e])
                    mysum -= p_list[d]
                mysum -= p_list[c]
            mysum -= p_list[b]
        mysum -= p_list[a]
    print "Best sum: %d" % best_sum
    if best_sum < 1000000:
        break;
    n *= 2
