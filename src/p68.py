#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=68

import math
import sys

# 1. To maximize the first digit, it must be 6 (with 7, 8, 9, and 10).
# 2. There are 5 sums, with total values of:
#       (6+7+8+9+10) + 2*(1+2+3+4+5) = 70,
# so each sum must be 14.
# 3. Consider possibilities:
# The 10 ring must include the pair (1,3) in some order.
# The 9 ring must include the pairs (1,4) or (2,3) in some order.
# The 8 ring must include the pairs (1,5) or (2,4) in some order.
# The 7 ring must include the pairs (2,5), or (3,4) in some order.
# The 6 ring must include the pair (3,5) in some order.
# 4. Observe that the 10 and 6 ring are determined (1,3) and (3,5) 
# respectively, with 3 now unavailable for the other triplets.
# 5. Since 3 is unavailable, the 9 triplet must be (9,1,4), with 1
# now unavailable.
# 6. Since 1 is unavailable, the 8 triplet must be (8,2,4), with 4
# now unavailable.
# 7. Since 4 is unavailable, the 7 triplet must be (7,2,5).
# 8. The triplets are:
#    (10,3,1)
#    (9,1,4)
#    (8,4,2)
#    (7,2,5)
#    (6,5,3)
# 9. The solution includes:
#   - we want to maximize 653 instead of 635
#   - this forces 725
#   - this forces 842
#   - this forces 914
#   - this forces 1031
#    
#         10
#           \
#            3     9
#          /   \ /
#         5     1
#       /  \ _ /__ 8
#      6    2  4
#            \ 
#             7

print "6531031914842725"
