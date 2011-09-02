#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=2

n1 = 1
n2 = 2
sum = 0
max = 4000000
n1_odd = True
n2_odd = False

while n1 < max:
    # Sum
    if not n1_odd:
        sum += n1

    # Next in the sequence
    t = n2
    n2 = n1 + n2
    n1 = t

    # Easy to compute odd/even
    t = n2_odd
    if n1_odd != n2_odd:
        n2_odd = True
    else:
        n2_odd = False
    n1_odd = t
    #print "n1=%d n2=%d n1_odd=%s n2_odd=%s" % (n1, n2, str(n1_odd), str(n2_odd))
print "sum=%d" % (sum)
