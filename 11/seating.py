#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Dec 11, 2020 17:37:08 AEDT
  @file        : seating

"""

import sys
import pprint

EMPTY_CHECK = 0
OCCUPIED_CHECK = 4

# Create 2D grid from input
def parseInput(inp):
    return [list(line) for line in inp.strip().split("\n")]

def updateGrid(grid):
    newGrid = [ [ updateSeat(grid,row,col) for col in range(len(grid[row])) ] for row in range(len(grid)) ]
    return newGrid

# Counts number of occupied seats around current seat
def countAround(grid, y, x):
    width  = len(grid[y])
    height = len(grid)

    numOccupied = 0

    for checkX in range(x-1, x+2):
        if checkX < 0 or checkX >= width: continue

        for checkY in range(y-1, y+2):
            # Don't check out of bounds
            if checkY < 0 or checkY >= height: continue

            # Don't include current seat in check
            if (checkY, checkX) == (y, x): continue
            
            # Add to count if seat is occupied
            numOccupied += (grid[checkY][checkX] == "#")

    return numOccupied

def updateSeat(grid, y, x):
    # We don't care about the floor
    if grid[y][x] == '.': return '.'
    
    switch = {"#": "L", "L": "#"}

    # confirm which count we want
    numToCount = [EMPTY_CHECK, OCCUPIED_CHECK][grid[y][x] == "#"]

    if y == 0 and x == 5:
        print(f"numToCount: {numToCount}, \
                countAround: {countAround(grid, y, x)}")

    # Switch them if count met
    if countAround(grid, y, x) >= numToCount:
        if y == 0 and x == 5:
            print("switching")
        return switch[grid[y][x]]

    # Otherwise keep the same
    # print("not switch")
    return grid[y][x]

# This time, write tests based on filepaths
inp = sys.stdin.read()
pprint.pprint(parseInput(inp))
print()
pprint.pprint(updateGrid(parseInput(inp)))
# print(countAround(parseInput(inp), 0, 5))

