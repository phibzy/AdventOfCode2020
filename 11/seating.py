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
    
    # confirm which count we want
    numToCount = [EMPTY_CHECK, OCCUPIED_CHECK][grid[y][x] == "#"]

    # Switch them if count met
    if grid[y][x] == "L" and countAround(grid, y, x) == numToCount:
        return "#" 

    if grid[y][x] == "#" and countAround(grid, y, x) >= numToCount:
        return "L"

    # Otherwise keep the same
    return grid[y][x]

def sumSeats(inp):
    return sum([1 for y in inp for x in y if x == "#"])

def updateGrid2(grid):
    newGrid = [ [ updateSeat2(grid,row,col) for col in range(len(grid[row])) ] for row in range(len(grid)) ]
    return newGrid

# Counts number of occupied seats around current seat
def countAround2(grid, y, x):
    width  = len(grid[y])
    height = len(grid)

    numOccupied = 0

    # zip - returns a 'zip object', an iterator of
    # tuples basically. Stops when either of the two
    # given iterators end.
    # Tl;dr length of iterator determined by shortest of two iterators
    # Look left
    # Misread question oops
    for i in range(x-1, -1, -1):
        if grid[y][i] == "#":
            numOccupied += 1
            break

        if grid[y][i] == "L": break

    # Look right
    for i in range(x+1, width):
        if grid[y][i] == "#":
            numOccupied += 1
            break

        if grid[y][i] == "L": break

    # Look up
    for i in range(y-1, -1, -1):
        if grid[i][x] == "#":
            numOccupied += 1
            break

        if grid[i][x] == "L": break

    # Look down
    for i in range(y+1, height):
        if grid[i][x] == "#":
            numOccupied += 1
            break

        if grid[i][x] == "L": break

    # Upright
    for i,j in zip(range(y-1, -1, -1), range(x+1, width)):
        if grid[i][j] == "#":
            numOccupied += 1
            break

        if grid[i][j] == "L": break

    # Downright
    for i,j in zip(range(y+1, height), range(x+1, width)):
        if grid[i][j] == "#":
            numOccupied += 1
            break

        if grid[i][j] == "L": break

    # Downleft
    for i,j in zip(range(y+1, height), range(x-1, -1, -1)):
        if grid[i][j] == "#":
            numOccupied += 1
            break

        if grid[i][j] == "L": break

    # Upleft
    for i,j in zip(range(y-1, -1, -1), range(x-1, -1, -1)):
        if grid[i][j] == "#":
            numOccupied += 1
            break

        if grid[i][j] == "L": break

    return numOccupied

def updateSeat2(grid, y, x):
    # We don't care about the floor
    if grid[y][x] == '.': return '.'
    
    # confirm which count we want
    numToCount = [EMPTY_CHECK, OCCUPIED_CHECK + 1][grid[y][x] == "#"]

    # Switch them if count met
    if grid[y][x] == "L" and countAround2(grid, y, x) == numToCount:
        return "#" 

    if grid[y][x] == "#" and countAround2(grid, y, x) >= numToCount:
        return "L"

    # Otherwise keep the same
    return grid[y][x]


# This time, write tests based on filepaths
inp = parseInput(sys.stdin.read())

newGrid = updateGrid(inp)

while newGrid != inp:
    inp = newGrid
    newGrid = updateGrid(newGrid)

print(sumSeats(inp))

# pprint.pprint(parseInput(inp))
# print()
# pprint.pprint(updateGrid(parseInput(inp)))
# print(countAround(parseInput(inp), 0, 5))

