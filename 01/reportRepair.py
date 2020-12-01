#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Dec 01, 2020 16:04:16 AEDT
  @file        : reportRepair

"""

import sys

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

# O(N^2) Solution to start with
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

def getInput():
    nums = list()

    for line in sys.stdin:
        nums.append(int(line))
    
    return nums

nums = getInput()

print(reportRepairPart2(nums))
