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
import pprint

def findValue(commands, visited, start):
    # Our total accumulated value
    total = 0

    # Easy way of dealing with signs
    signVal = {"+": 1, "-": -1}

    # flags for infinite loop, last nop/jmp indices
    inf, nops, jmps = False, list(), list()

    i = start
    while i < len(commands):
        # If we've seen exact instruction before, we have an infinite loop
        if i in visited: 
            inf = True
            break
        
        visited.setdefault(i, 0)

        instruction, sign, val = commands[i] 
        calc = signVal[sign]*int(val)

        # A jump instruction means we just change the index value
        if instruction == "jmp":
            # Keep track of visited indices at this point
            jmps.append((i, total, visited.copy()))

            # Plussing negatives is the same as minusing
            i += calc

        else:
            # acc instruction means we're adding to our total
            if instruction == "acc": 
                total += calc 

            else:
                # keep track of nop index, acc at this point as well as resulting index
                # if it were a jump instead
                nops.append((i, i + calc, total, visited.copy())) 

            # for nops and accs we keep going sequentially
            i += 1

    return (total, inf, jmps, nops)

# Algo: for each jump instruction in a looping list of commands, check if 
# changing it to nop fixes issue
# failing that do the same with the nop instructions
def fixedValue(commands):
    # dict that keeps track of visited indices
    visited = dict()

    # Have to preserve command list in each call, since we
    # could end up jumping backwards
    total, inf, jmps, nops = findValue(commands, visited, 0)

    if inf:

        for i, accTotal, v in jmps:
            nextTotal, inf, _, _ = findValue(commands, v, i + 1)

            # If there's no more infinite loops we're done here
            if not inf: return accTotal + nextTotal

        # for each nop, check if changing it to jmp results in terminating program
        for i, targetI, accTotal, v in nops:
            nextTotal, inf, _, _ = findValue(commands, v, targetI)

            if not inf: return accTotal + nextTotal

# function for parsing input so tests are easier
def parseInput(inp):
    return [ re.findall(r"^([a-z]{3}) ([\+\-])([0-9]+)", line)[0] for line in inp.strip().split('\n') ]

# commands = parseInput(sys.stdin.read())
# # # print(commands)
# pprint.pprint(findValue(commands, dict(), 0))
# print(fixedValue(commands))

