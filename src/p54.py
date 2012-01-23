#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=53

import math
import sys
import string

class Card:
    suit = None
    value = None
    _to_value = {"T":10, "J":11, "Q":12, "K":13, "A":14}
    _to_suit = {"C" : 0, "D" : 1, "H" : 2, "S": 3}

    def __init__(self, suit, value):
        self.suit = self._to_suit[suit]
        if value in self._to_value:
            self.value = self._to_value[value]
        else:
            self.value = int(value)

    def __cmp__(self, other):
        if self.suit < other.suit or (self.suit == other.suit and self.value < other.value):
            return -1
        elif self.suit == other.suit and self.value == other.value:
            return 0
        else:
            return 1
    def __str__(self):
        return "(%d, %d)" % (self.suit, self.value)

class Hand:
    cards = []

    def __init__(self):
        self.cards = []

    def add(self, c):
        card = Card(c[1], c[0])
        self.cards.append(card)
        self.cards = sorted(self.cards, reverse=True)
    
    def __str__(self):
        s = '('
        for i in range(len(self.cards)):
            if 0 < i:
                s += ', '
            s += str(self.cards[i])
        s += ')'
        return s

    def rank(self):
        is_flush = True
        is_straight = True
        occs = {self.cards[0].value : 1}
        values = [self.cards[0].value] 
        for i in range(1, len(self.cards)):
            if self.cards[0].suit != self.cards[i].suit:
                is_flush = False
            if self.cards[i].value in occs:
                occs[self.cards[i].value] += 1
            else:
                occs[self.cards[i].value] = 1
            values.append(self.cards[i].value)
        occs = sorted(occs.values(), reverse=True)
        values = sorted(values, reverse=True)
        for i in range(1, len(values)):
            if values[i-1] != values[i]+1:
                is_straight = False
                break;
        # special case
#        if values[0] == 14 and values[1] == 5 and values[2] == 4 and values[3] == 3 and values[4] == 2:
#            values = [5, 4, 3, 2, 1]
#            is_straight = True
        #print "occs: %s" % str(occs)
        if is_flush:
            if is_straight:
                if 14 == self.cards[0].value: 
                    # Royal Flush
                    return [10, values]
                else:
                    # Straight Flush
                    return [9, values]
        if 4 == occs[0] and 1 == occs[1]:
            # Four of a kind
            if values[0] == values[1]:
                return [8, values]
            else: 
                return [8, [values[1], values[2], values[3], values[4], values[0]]]
        elif 3 == occs[0] and 2 == occs[1]:
            # Full house
            if values[0] == values[1] and values[1] == values[2]:
                return [7, values]
            else :
                return [7, [values[2], values[3], values[4], values[0], values[1]]]
        elif is_flush:
            # Flush
            return [6, values]
        if is_straight:
            # Straight
            return [5, values]
        elif 3 == occs[0] and 1 == occs[1] and 1 == occs[2]:
            # Three of a kind
            if values[0] == values[1] and values[1] == values[2]: 
                return [4, values]
            elif values[1] == values[2] and values[2] == values[3]: 
                return [4, [values[1], values[2], values[3], values[0], values[4]]]
            else:
                return [4, [values[2], values[3], values[4], values[0], values[1]]]
        elif 2 == occs[0] and 2 == occs[1] and 1 == occs[2]:
            # Two pair
            if values[0] == values[1]:
                if values[2] == values[3]:
                    return [3, values]
                else:
                    return [3, [values[0], values[1], values[3], values[4], values[2]]]
            else:
                return [3, [values[1], values[2], values[3], values[4], values[0]]]
        elif 2 == occs[0] and 1 == occs[1] and 1 == occs[2] and 1 == occs[3]:
            # One pair
            if values[0] == values[1]:
                return [2, values]
            elif values[1] == values[2]:
                return [2, [values[1], values[2], values[0], values[3], values[4]]]
            elif values[2] == values[3]:
                return [2, [values[2], values[3], values[0], values[1], values[4]]]
            else:
                return [2, [values[3], values[4], values[0], values[1], values[2]]]
        elif 1 == occs[0] and 1 == occs[1] and 1 == occs[2] and 1 == occs[3] and 1 == occs[4]:
            # High card
            return [1, values]
        else:
            print "HERE"
            sys.exit(1)

if 2 != len(sys.argv):
    sys.stderr.write("Two arguments required!\n")
    sys.exit(1)

# read in file
fn = sys.argv[1]
f = open(sys.argv[1], 'r')
count = 0
for line in f.readlines():
    line = line.rstrip('\r\n')
    tokens = line.split()

    h1 = Hand()
    for i in range(5):
        h1.add(tokens[i])
    r1 = h1.rank()

    h2 = Hand()
    for i in range(5, 10):
        h2.add(tokens[i])
    r2 = h2.rank()

    win = None
    for i in range(6):
        if r1[i] < r2[i]:
            win = -1
            break
        elif r2[i] < r1[i]:
            win = 1
            break
    if None == win:
        print "ERROR"
        sys.exit(1)
    elif 0 < win:
        count += 1
    #print "[%s] r1: %s r2: %s win: %d" % (line, str(r1), str(r2), win)
f.close()

print "count:%d" % count
