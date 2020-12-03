#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 03, 2020 15:54:43 AEDT
  @file        : 03

"""

import sys

# Takes in a rule for how many spaces you move across (xPat),
# and how many down (yPat).
# TC: O(Y) - where Y is the length (y-axis) of grid
# SC: O(1)
def stepSearch(grid, xPat, yPat):
    width = len(grid[0])

    currLoc = [0, 0]
    treeCount = 0

    # While we haven't blown past bottom of screen
    while currLoc[0] < len(grid):
        # If we hit a tree count it
        # Do this first because some maps could start with
        # a tree
        if grid[currLoc[0]][currLoc[1]] == "#":
            treeCount += 1

        # Apply movement patterns
        currLoc[0] += yPat

        # We use % width here since the pattern repeats horizontally
        currLoc[1] = (currLoc[1] + xPat) % width

    return treeCount

# Takes in a grid and a list of rules for moving across/down
# TC: O(N) - where N is the number of slope rules
def totalTrees(grid, rules):
    # Since we're multiplying the results,
    # starting total has to be 1 otherwise result will
    # always be 0 (may or may not have made that mistake...)
    total = 1

    for x, y in rules:
        total *= stepSearch(grid, x, y)

    return total

inp = list()

# turn input into list
# for i in sys.stdin:
    # inp.append(list(i.strip()))

# print(totalTrees(inp, [[1,1],[3,1],[5,1],[7,1],[1,2]]))
