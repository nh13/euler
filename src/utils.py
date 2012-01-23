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
