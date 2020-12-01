#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Dec 01, 2020 16:04:16 AEDT
  @file        : reportRepair

"""

import sys

# TC: O(N) - We make one pass through the list of input
# SC: O(N) - Worst case last element is part of the sum,
#            meaning the dict becomes size N

# Very similar to TwoSum from Leetcode
def reportRepairPart1(nums, sumTarget):
    # Keep track of all items in list
    entries = dict()

    for i in nums:
        diff = sumTarget - i
        entries[i] = True
        
        if diff in entries:
            return i*diff

    # return -1 if we don't find two numbers that equal the target sum
    return -1

# TC: O(N^2) - Worst case make N/2 passes through list of length N/2 
# SC: O(N)   - Since we reuse the code from part 1
# Way to improve: Only add entries to dict on first pass
def reportRepairPart2(nums):
    # Keep track of all items in list
    # entries = dict()

    sumTarget = 2020

    for i,v in enumerate(nums):
        # We don't need to check behind us since we're checking forwards each time
        target = sumTarget - v
        
        check = reportRepairPart1(nums[i+1:], target)

        if check != -1:
            return check*v


# Me hurriedly scrapping together a quick way to read input lmao
def getInput():
    nums = list()

    for line in sys.stdin:
        # Convert lines to ints otherwise multiplication won't work
        # No need to strip newline characters from input
        nums.append(int(line))
    
    return nums

# Comment these out for testing
# nums = getInput()
# print(reportRepairPart2(nums))
