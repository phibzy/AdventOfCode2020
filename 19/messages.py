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

inp = parseInput(Path("./input/puzzle_input").read_text())

