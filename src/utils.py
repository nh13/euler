#!/usr/bin/env python

def contains_same_digits(a, b):
    a = str(a)
    b = str(b)
    for i in range(len(a)):
        found = False
        for j in range(len(b)):
            if a[i] == b[j]:
                b = b[0:j] + 'X' + b[j+1:len(b)]
                found = True
                break
        if not found:
            return found
    return True

def factorial(fact, n):
    if not n in fact:
        x = 1
        y = 1
        while x <= n:
            y *= x
            if not x in fact:
                fact[x] = y
            x += 1
    return fact[n]
