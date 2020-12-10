#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 10, 2020 16:11:52 AEDT
  @file        : adapter

"""

import sys

# Put rating as arg because I'm sure that will
# change in pt. 2 lmao
def findJoltDist(inp, rating):
    # Need to add 0 to list since charging outlet
    # joltage is 0
    # sort input to make diff calculations easy
    inp += [0]
    inp.sort()

    # counts for 1 and 3 differenes between jolts
    # your devices built-in adapter is always 3 higher than 
    # whatever your highest adapter is, so threeDiff starts at 1
    oneDiff, threeDiff = 0, 1

    # compare with previous element (since sorted),
    # increment counters if diff equals 1 or 3
    for i in range(1, len(inp)):
        diff = inp[i] - inp[i-1]

        # cheeky way of doing it
        oneDiff   += (diff == 1)
        threeDiff += (diff == 3)

    return oneDiff * threeDiff

# Get input into list
ratings = list(map(int, sys.stdin.readlines()))
print(findJoltDist(ratings, 3))
