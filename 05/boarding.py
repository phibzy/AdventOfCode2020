#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Dec 06, 2020 10:31:59 AEDT
  @file        : boarding

"""

import re, sys

ROWS = 127
COLS = 7

def decodeSeat(seat):
    # Get our row/col matches from string
    row, col = re.findall(r"^([FB]{7})([RL]{3})$", seat)[0]

    # Perform binary search on each
    # to get their number values
    rowNum = binSearch(row, ROWS)
    colNum = binSearch(col, COLS)

    return rowNum*8 + colNum

def binSearch(s, n):
    # if dealing with cols we use L/R,
    # otherwise we use F/B
    lowChar = ['F', 'L'][n == COLS]
    hiChar  = ['B', 'R'][n == COLS]

    start = 0
    end = n

    # Binary search - no early exit since
    # we always end up with one number
    for i in s:
        middle = start + (end - start) // 2

        if i == lowChar:
            end = middle

        elif i == hiChar:
            start = middle + 1

    return start

# Because we know that there are seats missing at the front/back
# of plane, we find the min/max seat numbers so we know what range of seatIDs
# we're dealing with
def findSeat(seats):
    maxSeat = max(seats)
    minSeat = min(seats)

    # Our seat number will be whatever number is missing in this range
    # We know what the sum of all numbers in this range SHOULD be, so we
    # can subtract the sum of our seatIDs and we will be left with
    # the missing number. TC is constant!
    return sum(range(minSeat, maxSeat + 1)) - sum(seats)

# Commented out so tests work
# inp = sys.stdin.read().splitlines()
# seats = list(map(decodeSeat, inp))
# print(findSeat(seats))

