#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 10, 2020 16:11:52 AEDT
  @file        : adapter

"""

import sys

# Get input into list
ratings = list(map(int, sys.stdin.readlines()))

# Put rating as arg because I'm sure that will
# change in pt. 2 lmao
def findJoltDist(inp, rating):
    # sort input
    inp.sort()

    # counts for 1 and 3 differenes between jolts
    # may need to make dict for pt. 2
    oneDiff, threeDiff = 0, 0

    # compare with previous element (since sorted),
    # increment counters if diff equals 1 or 3
    for i in range(1, len(inp)):
        diff = inp[i] - inp[i-1]

        # cheeky way of doing it
        oneDiff   += (diff == 1)
        threeDiff += (diff == 3)

    return oneDiff * threeDiff





# print(ratings)
