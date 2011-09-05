#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=31

import math
import sys

amt = 200
coins = (200, 100, 50, 20, 10, 5, 2, 1)

def func(amt, coins):
    #print "amt=%d coins=%s" % (amt, str(coins))
    if 0 == amt:
        return 1
    elif 1 == len(coins):
        if 0 == amt % coins[0]:
            return 1
        else:
            return 0
    else:
        sum = 0
        while 0 <= amt:
            sum += func(amt, coins[1:])
            amt -= coins[0]
        return sum

print "num=%d" % func(amt, coins)
