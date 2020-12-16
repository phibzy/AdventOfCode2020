#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Dec 16, 2020 10:37:26 AEDT
  @file        : docking

"""

import re

# Use dict to store memory address values
# Sum values at end

# Create a mask of 1 bits, then set any 0 bits needed
# We then and this mask with original number, which
# will give us our target number

# To parse input, grab mask first.
    # Set all Xs to 1s

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
        mask = int(re.sub("X", "1", g[0]), 2)

        # For each remaining line in the group, we want to grab
        # the number between the square brackets (memory address) and
        # the values after the equals sign
        commands = [ list(map(int, re.findall(r"^.*\[([0-9]+)\] = ([0-9]+)$", line)[0])) for line in g[1:] ]

        # Then add the group data to the output list,
        # since puzzle input has many groups like this with
        # different masks
        parsed.append([mask, commands])

    return parsed


