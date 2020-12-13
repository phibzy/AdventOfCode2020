#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Dec 13, 2020 12:16:51 AEDT
  @file        : rainRisk

"""

# N/S/E/W instructions don't change direction ship is facing
# Only L/R changes direction of ship - only have values of 90/180/270

from pathlib import Path

def parseInput(inp):
    # For each line in input, grab the first character (a letter)
    # and the rest of the line as an int. Make a list of these command combos.
    return [ [i[0], int(i[1:])] for i in inp.strip().split("\n") ]

def manhattanDistance(inp):
    # Keep track of how far we differ from origin
    # both vertically and horizontally
    # First element is horizontal, second is vertical
    distOrigin = [0,0]
    
    # Some constants for handling turning
    TURN = 90
    TURN_MULTIPLIER = [-1, 1]
    D_MOD = {"E": (0, 1), "S": (1, -1), "W": (0, -1), "N": (1, 1)}
    DIRECTIONS = ["E", "S", "W", "N"]
    NUM_DIRECTIONS = len(DIRECTIONS)

    currentDirection = 0

    # For each instruction and number
    for i, val in inp:
        # If we're turning, change the current direction
        if i == "L" or i == "R":
            # Since there are only 90/180/270 degree turns in input,
            # we divide value by 90 to check how many turns we make.
            # If we turn left, we're going backwards in the list so
            # we use a negative multiplier. Otherwise we use a positive one.
            # Mod result by number of directions so we have index of current
            # direction.
            currentDirection = (val // TURN)*TURN_MULTIPLIER[i == "R"]
            currentDirection %= NUM_DIRECTIONS

        elif i == "F":
            # Change dist origin based on current direction
            axis, multiplier = D_MOD[DIRECTIONS[currentDirection]]
            distOrigin[axis] += multiplier*val

        else:
            # Otherwise, move in given direction without changing where
            # ship is pointing
            axis, multiplier = D_MOD[i]
            distOrigin[axis] += multiplier*val

    # Get absolute vals of coords, then sum together
    return sum(map(abs, distOrigin)) 

inp = parseInput(Path("./input/puzzle_input").read_text())
print(manhattanDistance(inp))
