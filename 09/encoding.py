#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Dec 09, 2020 16:57:59 AEDT
  @file        : encoding

"""

import sys
from collections import deque

# preamble of 25 numbers, then a bunch of other numbers
# each number after preamble must be made result of addition of
# two different chars in the 25 digits before it

# First, create list/dict of first N numbers
def parsePreamble(inp, n):
    # nums keeps track of which numbers are in sequence,
    # order preserves their order
    nums = dict()
    order = deque()

    for i in range(n):
        nextNum = inp[i]

        nums.setdefault(nextNum, 0)
        nums[nextNum] += 1
        order.append(nextNum)

    # Return the dict and list
    return (nums, order)

# Find the odd number out based on constraints
# Assumes there is at least one such number in input
def findNumber(inp, n, nums, order):
    # start at the first index after preamble
    for i in range(n+1, len(inp)):
        nextNum = inp[i]

        # if current number isn't a sum of two different 
        # numbers in previous n numbers, it's WRONG
        if not checkSum(nextNum, nums):
            return nextNum

        # otherwise, slide the window of N characters
        # by updating nums and order by 1

        # First, remove oldest char
        deadNum = order.popleft()
        nums[deadNum] -=1
        if nums[deadNum] == 0: del nums[deadNum]

        # then add newest char
        order.append(nextNum)
        nums.setdefault(nextNum, 0)
        nums[nextNum] += 1

# see if there are two different numbers
# in sequence that add to target number
def checkSum(nextSum, nums):
    # TC always O(N), could do version with early exit but wanted to golf it
    return len([(x, nextSum - x) for x in nums if x != (nextSum - x) and (nextSum - x) in nums ]) > 0

# We'll use a sliding window for this
def findSequence(inp, targetSum):
    pass

# inp = list(map(int, sys.stdin.readlines()))
# N = 25
# print(findNumber(inp, N, *parsePreamble(inp, N)))
