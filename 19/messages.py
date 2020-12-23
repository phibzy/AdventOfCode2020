#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Tuesday Dec 22, 2020 11:20:46 AEDT
  @file        : messages

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
# This will return a valid flag as well as an index,
# so we don't lose track of our position
def checkValid(m, ruleDict, rule, i):


    # print("".rjust(30, "~"))
    # print(f"Calling rule {rule} at index {i}")
    # print()
    # Don't even bother if we've run out of string
    if i >= len(m): return []

    # Keep track of where we start for each call
    startIndex = i
    validIndices = list()

    # Remember it may be possible to reach end of string
    # before end of rule, so account for that
    for r in ruleDict[rule]:
        # Reset for each rule in list
        i = startIndex

        checkIndices = [i]
        for num in r:
            # print(f"At num {num} in subList {r}")
            nextList = list()

            # If it's a number, we need to call a rule
            if num.isdigit():
                for checkI in checkIndices:
                    iList = checkValid(m, ruleDict, num, checkI)
                    # print(f"Returning to {num} in subList {r}")
                    # print(f"iList is {iList}")

                    nextList += iList 
                    # print(f"Nextlist is {nextList}")
                    # print()
            
            # Otherwise it's a letter, so do a direct comparison
            else:
                # print("It's a letter!")
                for checkI in checkIndices:
                    if checkI >= len(m): continue
                    if m[checkI] == num:
                        # print("We match")
                        validIndices.append(checkI + 1)

            checkIndices = nextList

            # If there's no possible path of rules being upheld,
            # we're donezo
            if not nextList: break

        # If we've gone through the rules and we still have a
        # list of checkIndices - all elements in that list must be validIndices
        if checkIndices: validIndices += checkIndices

    # print(validIndices)
    return validIndices

# Pt. 1
# inp = parseInput(Path("./input/puzzle_input").read_text())

# Pt. 2
inp = parseInput(Path("./input/puzzle_input2").read_text())
print(checkMessages(*inp))
