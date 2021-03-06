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
    # print(groups)
    # print(''.rjust(30, "#"))
    for group in groups:
        # Separate mask and instructions
        g = group.strip().split("\n")
        
        # For the mask, we take the first line of the group
        # and change all X's into 1's, before converting it
        # as a binary string into an integer
        orMask   = int(re.sub("X", "0", g[0]), 2)
        andMask  = int(re.sub("X", "1", g[0]), 2)
        xMask1    = ''.join([ "1" if c == "X" else "0" for c in g[0] ])
        xMask2    = ''.join([ "0" if c == "X" else "1" for c in g[0] ])

        # For each remaining line in the group, we want to grab
        # the number between the square brackets (memory address) and
        # the values after the equals sign
        commands = [ list(map(int, re.findall(r"^.*\[([0-9]+)\] = ([0-9]+)$", line)[0])) for line in g[1:] ]

        # Then add the group data to the output list,
        # since puzzle input has many groups like this with
        # different masks
        parsed.append([xMask1, xMask2, orMask, andMask, commands])
        # print(f"og xmask: {xMask}")
        # print(xMask)

    return parsed

def sumMemory(inp):
    # Use a dict to keep track of memory addresses
    # Just have address 0 set to 0 for starters
    memory = {0: 0}

    for _, _, orMask, andMask, commands in inp:

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

def sumPt2(inp):
    memory = {0:0}

    for xMask1, xMask2, orMask, andMask, commands in inp:

        # keep track of indices of "floating" bits
        # get their power of 2. We do 35 - i since highest
        # power of 2 is 35 and most sig digit is furthest left
        floating = [ 2**(35-i) for i,v in enumerate(xMask1) if v == "1" ]

        for address, val in commands:
            # First up, OR with ormask to put in all the 1s
            # That are missing
            address |= orMask
            # Then AND with xMask2 to set all X bits to 0 initially
            # xMask2 is just a mask where all the X bits
            # are set to 0 and the others are set to 1
            address &= int(xMask2, 2)

            # We can also set our initial memory address
            memory[address] = val

            # Changing a binary digit is equivalent to
            # adding/subbing the power of 2
            # corresponding to that digit.

            # Therefore, we can get all the memory address
            # combinations by finding all the sum combinations for every
            # power of 2 corresponding to the Xs
            # Once that's done we just add each sum
            # to the base memory address

            # s stands for sums
            for s in genCombos(floating):
                nextA = address + s
                memory[nextA] = val


    return sum(memory.values())

# Function for getting all sum combinations
def genCombos(inp):
    if not inp: return []

    # First combo is always the current number by itself
    output = [ inp[0] ]

    # Grab the rest of the list and find 
    # all the possible combos in that sublist 
    rest = inp[1:]
    restCombos = genCombos(rest)

    # Then, add all those combos (i.e. all the sums
    # that don't include the current element), then 
    # create a new version of each sum that includes current element
    for val in restCombos:
        output.append(inp[0] + val)

    # Append all the sum combos not featuring current element
    output += restCombos

    return output

inp = parseInput(Path('./input/puzzle_input').read_text())
# inp = parseInput(Path('./input/test_input2').read_text())
# print(inp)

# Pt. 1
# print(sumMemory(inp))

# Pt. 2
print(sumPt2(inp))
