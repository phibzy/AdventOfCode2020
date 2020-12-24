#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Dec 23, 2020 19:02:27 AEDT
  @file        : jigsaw

"""

import numpy as np
from pathlib import Path
import re
from pprint import pprint

# Key note: outermost edges won't line up with ANY
# other tiles

"""
Algo:
    Create dict with image tile ID number as key

    Make vectors of edges for each tile
    These vectors, numbered 0 to 3 (where 0 is top edge,
    going clockwise until number 3 on left edge), will be
    tied to titleID

    Make universal dict with all vectors in it
    
    We'll then find the corner tiles by seeing which
    tiles have 2 edges that only show up oncein whole puzzle.

    Can do similar for border tiles (1 edge that shows up once).

    Can then do process of elimination for middle tiles,
    may need to do DFS/BFS for possibilities. 

    May have dict of dicts for tile IDs


    Will use Numpy for easy manipulation of grid

"""

def parseInput(inp):
    tileDict = dict()
    edgeDict = dict()

    # Split into groups separated by blank lines
    for tileGroup in inp.strip().split("\n\n"):
        tileID, grid = tileGroup.strip().split(":\n")

        # Grab tileID and convert to int
        tileID = int(re.findall(r"([0-9]+)", tileID)[0])
       
        # Turn the grid into a np array
        grid = np.array([ [ char for char in line ] for line in grid.strip().split("\n") ])
        pprint(grid)

        # Grab the edges
        topRow = grid[:1]
        bottomRow = grid[-1:]
        leftCol = np.reshape(grid[:,:1], (1,10))
        rightCol = np.reshape(grid[:,-1:], (1,10))

        # Put them into dict, with edge order preserved
        tileDict[tileID] = [topRow, rightCol, bottomRow, rightCol]


        # Weird case: multiple of same edge in tile, but unique to tile

# inp = Path("./input/puzzle_input").read_text()
inp = Path("./input/test1").read_text()
parseInput(inp)
