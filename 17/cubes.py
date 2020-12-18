#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Dec 18, 2020 14:36:14 AEDT
  @file        : cubes

"""

from pathlib import Path
import pprint

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

inp = Path("./input/puzzle_input").read_text()
parseSlice(inp)
