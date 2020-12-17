#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 17, 2020 14:24:57 AEDT
  @file        : translation

"""

import re

# Split on 2\n's
# For first group, want to grab name and ranges and place
# in dict
# Optional: Combine ranges where applicable

# Put your ticket's vals in list

# Do lists for other tickets
# Add up all values which are invalid

def parseInput(inp):
    # Split as mentioned above
    rules, yourTix, otherTix = inp.split("\n\n")

    fieldRules = dict()
    for line in rules.split("\n"):
        field, range1s, range1e, range2s, range2e = re.findall("^(.*): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)$", line)[0]
        fieldRules[field] = [[int(range1s), int(range1e)], [int(range2s), int(range2e)]]

    myVals = list(map(int, yourTix.split("\n")[1].split(",")))

    otherTix = otherTix.strip().split("\n")[1:]
    for i in range(len(otherTix)):
        otherTix[i] = list(map(int, otherTix[i].split(",")))

    return (fieldRules, myVals, otherTix)
    


