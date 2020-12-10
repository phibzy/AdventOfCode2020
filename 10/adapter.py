#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 10, 2020 16:11:52 AEDT
  @file        : adapter

"""

import sys
import logging

# Put rating as arg because I'm sure that will
# change in pt. 2 lmao - EDIT: IT DIDN'T
def findJoltDist(inp):
    # Need to add 0 to list since charging outlet
    # joltage is 0
    # sort input to make diff calculations easy
    inp += [0]
    inp.sort()

    # counts for 1 and 3 differenes between jolts
    # your devices built-in adapter is always 3 higher than 
    # whatever your highest adapter is, so threeDiff starts at 1
    oneDiff, threeDiff = 0, 1
    diffs = list()

    # compare with previous element (since sorted),
    # increment counters if diff equals 1 or 3
    for i in range(1, len(inp)):
        diff = inp[i] - inp[i-1]
        diffs.append(diff)

        # cheeky way of doing it
        oneDiff   += (diff == 1)
        threeDiff += (diff == 3)

    return (oneDiff * threeDiff, diffs)

# Will do DFS brute force method first
def findPossiblePaths(inp):
    # Need to add 0 to list since charging outlet
    # joltage is 0
    # sort input to make diff calculations easy
    inp += [0]
    inp.sort()

    # print(f"inp: {inp}")

    return rDFS(inp, dict(), 0)

# DFS with DP    
def rDFS(inp, visited, start):
    # print("".rjust(20, "#"))
    # Base case - no more numbers, only 1 path
    # Do the same when we overshoot end of array
    if start >= len(inp) - 1: return 1

    total = 1

    # If already visited return the path value
    if start in visited: return visited[start]

    # Otherwise, check next 3 elements if valid
    # and get their paths
    currTotal = total
    total*= rDFS(inp, visited, start + 1)

    l, r = 0,0

    if start + 2 < len(inp) and (inp[start+2] - inp[start] <= 3):
        l = currTotal*rDFS(inp, visited, start + 2)

    if start + 3 < len(inp) and (inp[start+3] - inp[start] <= 3):
        r = currTotal*rDFS(inp, visited, start + 3)
    
    total = total + l + r

    visited[start] = total
    return total

# Get input into list
ratings = list(map(int, sys.stdin.readlines()))
# print(findJoltDist(ratings))
print(findPossiblePaths(ratings))
