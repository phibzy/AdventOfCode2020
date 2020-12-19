#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Saturday Dec 19, 2020 12:29:53 AEDT
  @file        : pt2

"""

# Pt.2 - using numpy arrays since things were getting way too messy

import numpy as np
from pathlib import Path
from copy import deepcopy
from pprint import pprint

def parseInput(inp):
    # Our slice is going to be a 2d list 
    sl = list()
    
    # Have to convert to list since strings
    # can't be modified, even though they're technically lists
    for line in inp.strip().split("\n"):
        # Add in the col padding while we're here
        sl.append(['.'] + list(line) + ['.'])

    sl = [[ '.' for _ in range(len(sl[0])) ]] + sl + [[ '.' for _ in range(len(sl[0])) ]]

    # Create numpy array of 2d slice
    sl = np.array(sl)

    # Create blank 2d slices for padding in 3d plane
    # blankFace = np.full((len(sl[0]), len(sl)), '.')

    # Create 3d space
    zSpace = np.array([np.full((len(sl), len(sl[0])), '.'), sl, np.full((len(sl), len(sl[0])), '.')])

    # Create 4d space
    wSpace = np.array([ np.full( (len(zSpace), len(zSpace[0]), len(zSpace[0][0])), '.'),
                        zSpace,
                        np.full((len(zSpace),  len(zSpace[0]),  len(zSpace[0][0])), '.')])

    return wSpace

def cycle(inp):
    # flags for end if we need to expand
    topRow = bottomRow = leftCol = rightCol = topPlane = bottomPlane = topSpace = bottomSpace = False
    
    # how many active cubes we have
    activeCount = 0

    # Make copy of current space
    # since we're updating all cubes simultaneously
    # Do deep copy since it's a 4D list
    newInp = deepcopy(inp)

    # Keeping track of max dimensions
    wLength = len(inp)
    zLength = len(inp[0])
    yLength = len(inp[0][0])
    xLength = len(inp[0][0][0])

    # pprint.pprint(inp)
    # pprint.pprint(newInp)

    # Here we go
    for w in range(wLength):
        for z in range(zLength):
            for y in range(yLength):
                for x in range(xLength):

                    # Update new cube based on current one 
                    newInp[w][z][y][x] = updateSpace(inp, w, z, y, x, wLength, zLength, yLength, xLength)

                    # if we have a new active case
                    # in the padding, set flags for which parts
                    # of padding need expanding
                    if newInp[w][z][y][x] == "#":
                        activeCount += 1

                        if w == 0:
                            topSpace = True

                        elif w == wLength - 1:
                            bottomSpace = True

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

                # pprint.pprint(newInp)

                # print(f"val: {newInp[z][y][x]}")
    
    # print("".rjust(30, '$'))
    # pprint.pprint(newInp)
    print(activeCount)

    # print("".rjust(30, '$'))
    # print("".rjust(30, '$'))
    # Expand newInp based on flags
    # Use new list comprehensions for each row/plane this time ;)
    expandGrid(newInp, topSpace, bottomSpace, topPlane, bottomPlane, topRow, bottomRow, leftCol, rightCol)

    # pprint.pprint(newInp)

    return (newInp, activeCount)

def updateSpace(inp, w, z, y, x, wLength, zLength, yLength, xLength):
    active = (inp[w][z][y][x] == "#")
    # pprint.pprint(inp)
    # print(active)

    # in both cases, if we have more than
    # three active neighbours we can do an early exit
    # and return inactive
    activeMax = 3 
    activeCount = 0

    # Error was I forgot to add extra one
    # since ranges don't include endpoint
    wBoundLow, wBoundHi = max(0, w-1), min(wLength - 1, w + 1) + 1 
    zBoundLow, zBoundHi = max(0, z-1), min(zLength - 1, z + 1) + 1 
    yBoundLow, yBoundHi = max(0, y-1), min(yLength - 1, y + 1) + 1 
    xBoundLow, xBoundHi = max(0, x-1), min(xLength - 1, x + 1) + 1 

    for nW in range(wBoundLow, wBoundHi):
        for nZ in range(zBoundLow, zBoundHi):
            for nY in range(yBoundLow, yBoundHi):
                for nX in range(xBoundLow, xBoundHi):

                    # Don't count current cube as neighbour!
                    if (w,z,y,x) == (nW, nZ, nY, nX): continue

                    # increment count if neighbour is active
                    activeCount += (inp[nW][nZ][nY][nX] == "#")
                    
                    # early exit if too many active neighbours
                    if activeCount > 3: return "."

    if active and (activeCount == 2 or activeCount == 3):
        return "#"

    elif (not active) and (activeCount == 3):
        return "#"

    return "."


# One of these expansions isn't working properly
def expandGrid(newInp, topSpace, bottomSpace, topPlane, bottomPlane, topRow, bottomRow, leftCol, rightCol):
    # print(f"topSpace: {topSpace}, bottomSpace: {bottomSpace}, topPlane: {topPlane}, bottomPlane: {bottomPlane}, topRow: {topRow}, bottomRow: {bottomRow}, leftCol: {leftCol}, rightCol: {rightCol}")

    # print(f"newInp dim is: {newInp.shape}")

    # First handle columns
    if leftCol:
        newInp = np.array([np.full((len(newInp), len(newInp[0]), len(newInp[0][0]), 1), '.'), newInp])
        # print(f"newInp dim is: {newInp.shape}")

    if rightCol:
        newInp = np.array([newInp, np.full((len(newInp), len(newInp[0]), len(newInp[0][0]), 1), '.')])
        # print(f"newInp dim is: {newInp.shape}")

    # Then rows
    if topRow:
       newInp = np.append(np.full((len(newInp), len(newInp[0]), 1, len(newInp[0][0][0])), '.'), newInp, axis=2) 
       # print(f"newInp dim is: {newInp.shape}")

    if bottomRow:
       newInp = np.append(newInp, np.full((len(newInp), len(newInp[0]), 1, len(newInp[0][0][0])), '.'), axis=2)
       # print(f"newInp dim is: {newInp.shape}")

    # Then planes
    if topPlane:
       newInp = np.append(np.full((len(newInp), 1, len(newInp[0][0]), len(newInp[0][0][0])), '.'), newInp, axis=1) 
       # print(f"newInp dim is: {newInp.shape}")

    if bottomPlane:
       newInp = np.append(newInp, np.full((len(newInp), 1, len(newInp[0][0]), len(newInp[0][0][0])), '.'), axis=1) 
       # print(f"newInp dim is: {newInp.shape}")

    # Then 4th D
    if topSpace:
        newInp = np.array([np.full((1, len(newInp[0]), len(newInp[0][0]), len(newInp[0][0][0])), '.'), newInp])
        # print(f"newInp dim is: {newInp.shape}")

    if bottomSpace:
        newInp = np.array([ newInp, np.full((1, len(newInp[0]), len(newInp[0][0]), len(newInp[0][0][0])), '.') ])
        # print(f"newInp dim is: {newInp.shape}")

# Assumes at least 1 cycle will be run
def runCycles(inp, numCycles):
    
    for _ in range(numCycles):
        inp, numActive = cycle(inp)

    return numActive

inp = parseInput(Path("./input/puzzle_input").read_text())
print(inp)
