#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Dec 22, 2020 11:20:46 AEDT
  @file        : messages

  My part 1 originally had a bug but it passed the check anyway/

  Original part 1 always instantly terminated a recursive call if it
  found a valid path. This was problematic because different valid
  paths return different finishing indices. So while yes, it was valid
  for some condition of a rule, in the long run it wouldn't validate 
  some messages since these messages depended on particular
  validation paths. So I changed it to explore every possible
  validation path.

"""

from pathlib import Path
from pprint import pprint
import re

def parseInput(inp):
    rules, messages = inp.split("\n\n")

    ruleDict = dict()

    # Create a dict with rule numbers as keys
    # For values, we'll use a list of lists (to keep track of OR conditions)
    # Each sublist will be condition that has to be met
    # Split the sublists on spaces to arrange rule numbers nicely
    for r in rules.strip().split("\n"):
        ruleNo, rL = re.findall(r"^([0-9]+)\: (.*)", r)[0]
        rL = re.sub('"', '', rL) 
        rL = rL.split("|")
        rL = [ list(filter(None, x.split(" "))) for x in rL ]
        ruleDict[ruleNo] = rL

    # Put all the messages in one list too
    msgList = messages.strip().split("\n")

    return (ruleDict, msgList)

def checkMessages(ruleDict, msgList):
    total = 0

    # Check if each message is valid according to rule 0
    # increment our counter if it is
    for m in msgList:
        validList = checkValid(m, ruleDict, "0", 0)

        # Check that none of the valid checks
        # left off the end of the string
        valid = [ v for v in validList if v == len(m) ]

        # Add to total if valid
        if valid:
            total += 1

    return total

# Recursion time!
# This function returns a list of indexes
# These indexes are used as starting points
# for the next recursive calls
def checkValid(m, ruleDict, rule, i):
    # If we've gone past the end of the list,
    # there's no way it can be valid
    if i >= len(m): return []

    # Keep track of where we start for each call
    startIndex = i
    validIndices = list()

    # Remember it may be possible to reach end of string
    # before end of rule, so account for that
    for r in ruleDict[rule]:
        # Reset for each rule in list
        i = startIndex
        
        # We use a list of checkIndices because
        # we want to keep track of all the different
        # ways a string could be valid. While it may match
        # the first possible condition, later on down the track
        # it may turn out that another condition is the only
        # one that leads to the full message being considered valid
        checkIndices = [i]
        for num in r:
            nextList = list()

            # If it's a number, we need to call a rule
            if num.isdigit():
                # For each different starting index,
                # check the rule is valid
                for checkI in checkIndices:
                    # See if there's any valid starting indices
                    iList = checkValid(m, ruleDict, num, checkI)
                    nextList += iList 
            
            # Otherwise it's a letter, so do a direct comparison
            else:
                for checkI in checkIndices:
                    if checkI >= len(m): continue
                    if m[checkI] == num:
                        validIndices.append(checkI + 1)

            checkIndices = nextList

            # If there's no possible path of rules being upheld,
            # we're donezo
            if not nextList: break

        # If we've gone through all the rules and we still have a
        # list of checkIndices - all elements in that list must be validIndices
        if checkIndices: validIndices += checkIndices

    return validIndices

# Pt. 1
# inp = parseInput(Path("./input/puzzle_input").read_text())

# Pt. 2
inp = parseInput(Path("./input/puzzle_input2").read_text())
print(checkMessages(*inp))
