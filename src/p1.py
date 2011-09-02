#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=1

sum = 0
i3 = 3
i5 = 5
max = 1000
while i3 < max or i5 < max:
    if i3 < i5:
        sum += i3
        i3 += 3
    elif i3 == i5:
        sum += i3
        i3 += 3
        i5 += 5
    else:
        sum += i5
        i5 += 5
    #print "i3=%d i5=%d sum=%d" % (i3, i5, sum)
print "sum=%d" % sum
