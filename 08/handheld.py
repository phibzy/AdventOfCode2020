#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Dec 08, 2020 21:03:35 AEDT
  @file        : handheld

"""

"""
Algo:
    Make list of insructions (parsed)
    Use indexes for jumping
    If we visit any index more than once, we're in a loop

"""
import re, sys

def findValue(commands):
    # dict that keeps track of visited indices
    visited = dict()
    
    # Our total accumulated value
    total = 0

    # Easy way of dealing with signs
    signVal = {"+": 1, "-": -1}

    i = 0
    while i < len(commands):
        # If we've seen exact instruction before, we have an infinite loop
        if i in visited: break
        visited.setdefault(i, 0)

        instruction, sign, val = commands[i] 
        
        # A jump instruction means we just change the index value
        if instruction == "jmp":

            # Plussing negatives is the same as minusing
            i += signVal[sign]*int(val)

        else:
            # acc instruction means we're adding to our total
            if instruction == "acc": 
                total += signVal[sign]*int(val)

            # for nops and accs we keep going sequentially
            i += 1

    return total

commands = [ re.findall(r"^([a-z]{3}) ([\+\-])([0-9]+)", line)[0] for line in sys.stdin.read().strip().split('\n') ]

print(findValue(commands))


