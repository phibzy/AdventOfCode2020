#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Dec 18, 2020 14:36:14 AEDT
  @file        : cubes

"""

from pathlib import Path
import pprint
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(msg)s")

# Create representation of cube
# Because this cube can keep growing,
# we'll add extra rows/columns/levels around the perimeter
# (2 cols, 2 rows, 2 levels) to check if it needs extending

# Have something to check if extra plane/rows/cols were added

# Get our starting slice and turn it into 3d space 
def parseSlice(inp):
    # Our slice is going to be a 2d list 
    sl = list()

    # Have to convert to string since strings
    # can't be modified, even though they're technically lists
    for line in inp.strip().split("\n"):
        # Add in the col padding while we're here
        sl.append(['.'] + list(line) + ['.'])

    # Add in the row padding 
    rPadding = [ '.' for _ in range(len(sl[0])) ]
    sl = [rPadding] + sl + [rPadding]

    # Create our 3d spaaaaace
    space = list()

    # Create a completely inactive 2d slice of padding
    padSlice = [ [ "."  for col in row ] for row in sl ]

    # Pad our 2d slice with slices on top and bottom
    space.append(padSlice) 
    space.append(sl) 
    space.append(padSlice) 

    return space

def cycle(inp):
    # flags for end if we need to expand
    topRow = bottomRow = leftCol = rightCol = topPlane = bottomPlane = False
    
    # how many active cubes we have
    activeCount = 0

    # Make copy of current space
    # since we're updating all cubes simultaneously
    newInp = inp.copy()

    # Keeping track of max dimensions
    zLength = len(inp)
    yLength = len(inp[0])
    xLength = len(inp[0][0])

    # Here we go
    for z in range(zLength):
        for y in range(yLength):
            for x in range(xLength):

                # Update new space based on current one 
                newInp[z][y][x] = updateCube(inp, z, y, x, zLength, yLength, xLength)

                # if we have a new active case
                # in the padding, set flags for which parts
                # of padding need expanding
                if newInp[z][y][x] == "#":
                    activeCount += 1

                    if z == 0:
                        topPlane = True

                    elif z == zLength - 1:
                        bottomPlane = True

                    if y == 0:
                        topRow = True

                    elif y == yLength - 1:
                        bottomRow = True

                    if x == 0:
                        leftCol = True

                    elif x == xLength - 1:
                        rightCol = True

    # Expand newInp based on flags
    # pprint.pprint(newInp)        
    return (newInp, activeCount)


def updateCube(inp, z, y, x, zLength, yLength, xLength):
    active = (inp[z][y][x] == "#")
    pprint.pprint(inp)

    # in both cases, if we have more than
    # three active neighbours we can do an early exit
    # and return inactive
    activeMax = 3 
    activeCount = 0

    # Error was I forgot to add extra one
    # since ranges don't include endpoint
    zBoundLow, zBoundHi = max(0, z-1), min(zLength - 1, z + 1) + 1 
    yBoundLow, yBoundHi = max(0, y-1), min(yLength - 1, y + 1) + 1 
    xBoundLow, xBoundHi = max(0, x-1), min(xLength - 1, x + 1) + 1 

    for nZ in range(zBoundLow, zBoundHi):
        for nY in range(yBoundLow, yBoundHi):
            for nX in range(xBoundLow, xBoundHi):

                # Don't count current cube as neighbour!
                if (z,y,x) == (nZ, nY, nX): continue

                # increment count if neighbour is active
                activeCount += (inp[nZ][nY][nX] == "#")
                
                # early exit if too many active neighbours
                if activeCount > 3: return "."

    # print(f"activeCount: {activeCount}")

    if active and (activeCount == 2 or activeCount == 3):
        return "#"

    elif not active and (activeCount == 3):
        return "#"

    return "."

"""
Notes:
    - Expand space at end of cycle if necessary
        - Have flags for left/right row/col/plane 

    - Counting neighbours
        - Check whether active/inactive to find max
          value, helps with early exit


"""

# inp = parseSlice(Path("./input/puzzle_input").read_text())
inp = parseSlice(Path("./input/test_input").read_text())
# cycle(inp)
# logging.debug("POOPOO")