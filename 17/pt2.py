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

    print(wSpace)

    # return space

inp = parseInput(Path("./input/puzzle_input").read_text())

