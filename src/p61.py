#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=61

import math
import sys

def triangle(n):
    return n * (n + 1) / 2

def square(n):
    return n * n

def pentagonal(n):
    return n * ((3 * n) - 1) / 2

def hexagonal(n):
    return n * ((2 * n) - 1)

def heptagonal(n):
    return n * ((5 * n) - 3 ) / 2

def octagonal(n):
    return n * ((3 * n) - 2)

def compute(n, which):
    return {3 : triangle(n),
            4 : square(n),
            5 : pentagonal(n),
            6 : hexagonal(n),
            7 : heptagonal(n),
            8 : octagonal(n)}[which]

def binary_search(arr, n):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class Node:
    def __init__(self, value):
        self.value = value
        self.which = {}
        for i in range(3, 9):
            self.which[i] = False

    def add_which(self, which):
        self.which[which] = True

    def contains_which(self, which):
        return self.which[which]

class Graph:
    def __init__(self):
        self.nodes = {}
        self.f2b = {} # 8128, 8129: 81 => [**81, **81, ...]
        self.b2f = {} # 8128, 8228: 28 => [28**, 28**, ...]

    def add(self, value, which):
        if not value in self.nodes:
            self.nodes[value] = Node(value)
        self.nodes[value].add_which(which)
        x = value / 100
        if not x in self.f2b:
            self.f2b[x] = []
        self.f2b[x].append(value)
        y = value % 100
        if 10 <= y:
            if not y in self.b2f:
                self.b2f[y] = []
            self.b2f[y].append(value)

    def finalize(self):
        for i in self.f2b.keys():
            self.f2b[i] = sorted(self.f2b[i])
        for i in self.b2f.keys():
            self.b2f[i] = sorted(self.b2f[i])

    def search(self):
        # states to maintain
        nums = [] # the numbers
        idx = [] # index into bf2
        nodes = sorted(self.nodes.keys())
        sums = []

        # init
        for i in range(len(nodes)):
            y = nodes[i] % 100
            if y in self.f2b:
                nums.append(nodes[i])
                idx.append(-1)
                start = i
                break
        
        # TODO: why do we repeat searches?
        # search
        while start < len(nodes):
            if 0 == len(nums):
                nums.append(nodes[start])
                idx.append(-1)

            idx[len(nums)-1] = idx[len(nums)-1] + 1
            x = nums[len(nums)-1]
            i = idx[len(nums)-1] 
            y = x % 100
            
            if len(nums) == 6 and (nums[len(nums)-1] % 100) == (nums[0] / 100):
                mat = [[self.nodes[nums[i]].which[j+3] for i in range(len(nums))] for j in range(len(nums))]
                found = True
                # test if the potential solution is valid
                for i in range(len(nums)):
                    for j in range(i+1, len(nums)):
                        # row by row
                        n = 0
                        m = 0
                        for k in range(len(nums)): 
                            if mat[i][k] or mat[j][k]:
                                n = n + 1
                            if mat[k][i] or mat[k][j]:
                                m = m + 1
                        if n <= 1 or m <= 1:
                            found = False
                            break
                    if not found:
                        break
                if found:
                    sys.stderr.write("Found = %s\n" % str(found))
                    sys.stderr.write("Nums = %s\n" % str(nums))
                    sys.stderr.write("Sum = %d\n" % sum(nums))
                    if not sum(nums) in sums:
                        sums.append(sum(nums))
                    for num in nums:
                        print "%d => %s" % (num, str(self.nodes[num].which))
                    break # find only the first one
            if len(nums) < 6 and y in self.f2b and i < len(self.f2b[y]):
                # recurse
                nums.append(self.f2b[y][i])
                idx.append(-1)
            else:
                # backtrack
                del nums[-1]
                del idx[-1]
            if 0 == len(nums):
                start = start + 1

# generate all possible 4-digit triangles, squares, pentagonals, hexagonals, 
# heptagonals, and octagonals
graph = Graph()
for which in range(3, 9):
    i = 1
    n = 1
    while n < 10000:
        n = compute(i, which)
        #print "n=%d i=%d which=%d" % (n, i, which)
        if 1000 <= n and n < 10000:
            graph.add(n, which)
        i += 1
graph.finalize()
graph.search()
