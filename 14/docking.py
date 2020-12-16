#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Dec 16, 2020 10:37:26 AEDT
  @file        : docking

"""

import re
from pathlib import Path

# For each XMask given, create a mask where all Xs are
# set to 0 (orMask) and one where all Xs are set to one (andMask)

# For each value we need to change, we first OR the value with
# our orMask - which will set all 1 bits that need to be set

# We then AND this result with our andMask to set all
# the 0 bits. We're basically abusing the fact that 1 AND 0 is 0

# We'll then use a dict to store these values at memory address keys
# so they're easy to rewrite and then sum all values in dict

# To parse input, grab mask first and create our and/orMasks
# Then grab mem addresses and values on each line after
def parseInput(inp):
    # Split on masks
    # Will have empty string at start so ignore that
    groups = inp.split("mask = ")[1:]

    parsed = list()

    # For each group of masks and instructions
    for group in groups:
        # Separate mask and instructions
        g = group.strip().split("\n")
        
        # For the mask, we take the first line of the group
        # and change all X's into 1's, before converting it
        # as a binary string into an integer
        orMask   = int(re.sub("X", "0", g[0]), 2)
        andMask  = int(re.sub("X", "1", g[0]), 2)

        # For each remaining line in the group, we want to grab
        # the number between the square brackets (memory address) and
        # the values after the equals sign
        commands = [ list(map(int, re.findall(r"^.*\[([0-9]+)\] = ([0-9]+)$", line)[0])) for line in g[1:] ]

        # Then add the group data to the output list,
        # since puzzle input has many groups like this with
        # different masks
        parsed.append([orMask, andMask, commands])

    return parsed

def sumMemory(inp):
    # Use a dict to keep track of memory addresses
    # Just have address 0 set to 0 for starters
    memory = {0: 0}

    for orMask, andMask, commands in inp:

        for address, val in commands:
            # First, OR with the ormask to add in 
            # any missing 1s
            val |= orMask

            # Then AND with the andmask to add in
            # any 0s that should be there
            val &= andMask

            # Set the value in memory
            memory[address] = val

    # Return the sum of all the values in memory
    return sum(memory.values())

inp = parseInput(Path('./input/puzzle_input').read_text())

# Pt. 1
print(sumMemory(inp))
