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

    return rDFS(inp, dict(), 0)

    
def rDFS(inp, visited, start):
    # Diffs are only 1 or 3 (I checked)
    total = 1

    while start < len(inp):
        # If we've visited somewhere before,
        # we just multiply what we have with the visited spot,
        # because we know that the rest would have been visited too
        if start in visited:
            total *= visited[start]
            break

        diff = inp[start] - inp[start - 1]

        # A diff of 3 means there's only one path to the number
        # after the next one
        if diff != 3:
            currT = total

            if start + 1 < len(inp) and (inp[start+1] - inp[start-1] <= 3):
                visited[start + 1] = rDFS(inp, visited, start+1)
                total += currT*visited[start + 1]

            if start + 2 < len(inp) and (inp[start+2] - inp[start-1] <= 3):
                visited[start + 2] = rDFS(inp, visited, start+2)
                total += currT*visited[start + 2]

        start += 1

    visited[start] = total
    return total



# Get input into list
# ratings = list(map(int, sys.stdin.readlines()))
# print(findJoltDist(ratings))
