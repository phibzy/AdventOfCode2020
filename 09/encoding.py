#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Dec 09, 2020 16:57:59 AEDT
  @file        : encoding

"""

# preamble of 25 numbers, then a bunch of other numbers
# each number after preamble must be made result of addition of
# two different chars in the 25 digits before it

# First, create list/dict of first N numbers
def parsePreamble(inp, n):
    # nums keeps track of which numbers are in sequence,
    # order preserves their order
    nums = dict()
    order = list()

    for i in range(n):
        nextNum = int(inp[i])

        nums.setdefault(nextNum, 0)
        nums[nextNum] += 1
        order.append(nextNum)

    # Return the dict and list
    return (nums, order)
