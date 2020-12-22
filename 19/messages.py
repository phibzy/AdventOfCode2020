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
        v, i = checkValid(m, ruleDict, "0", 0)

        # If there's still string remaining after the rules
        # have been checked, it can't be valid
        if i != len(m): v = False

        if v:
            print(f"{m} is valid!")

        # Add to total if valid
        total += v

    return total

# Recursion time!
# This will return a valid flag as well as an index,
# so we don't lose track of our position
def checkValid(m, ruleDict, rule, i):
    print()
    print("".rjust(30, "~"))
    print("New call" + "".rjust(20, "-"))
    print(f"rule: {rule}, i: {i}")

    print("".rjust(28, "-"))

    # Keep track of where we start for each call
    startIndex = i
    valid = False

    # Remember it may be possible to reach end of string
    # before end of rule, so account for that
    for r in ruleDict[rule]:
        # Reset for each rule in list
        i = startIndex
        print(f"rule: {rule}, subRule: {r}, i: {i}")
        valid = False

        for num in r:
            # Break if we run out of string
            if i >= len(m): 
                print(f"Run out of string on {num} in subList {r} in {rule}...")
                valid = False
                break

            print(f"curr char: {m[i]}")
            # If it's a number, we need to call a rule
            if num.isdigit():
                print(f"Calling rule {num} from {rule} in group {r}...")
                valid, i = checkValid(m, ruleDict, num, i)
                print(f"Coming back to group {r} from {rule} ...")
            
            # Otherwise it's a letter, so do a direct comparison
            else:
                valid = (m[i] == num) 
                i += 1
            
            # If the rule doesn't hold, don't bother checking further
            if not valid: 
                # print(f"rule {r} does not hold for {i}: {m[i]}")
                break

        # This needs changing
        # if one of the list of rules holds, it's valid!
        if valid: break

    return (valid, i)

# inp = parseInput(Path("./input/puzzle_input").read_text())
inp = parseInput(Path("./input/test4").read_text())
# inp = parseInput(Path("./input/puzzle_input2").read_text())
# print(checkMessages(*inp))
# print(checkValid("aaaaabbaabaaaaababaa", inp[0], "0", 0))
