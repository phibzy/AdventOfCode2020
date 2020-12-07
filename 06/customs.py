#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Dec 07, 2020 13:43:09 AEDT
  @file        : customs

"""

import sys

# add flags for pt 1 and pt 2

def totalCount(s, f):
    # Split on blank lines
    groupForms = s.split("\n\n")
    total = 0

    for group in groupForms:
        total += groupCount(group.strip().split(), f)

    return total

# Takes in list of strings representing each form in 
# a group
def groupCount(group, f):
    # Dict keeping track of how many different qs
    # had a yes answer in the group
    qDict = dict()

    # List keeping track of how many qs everyone answered yes to
    allYes = list()

    # For each form in group, find each
    # unique question in each form
    for form in group:
        for q in form:

            # We should only be dealing with lowercase a-z
            if q < "a" or q > "z": continue

            qDict.setdefault(q, 0)
            qDict[q] += 1

            # If question has shown up an amount of times
            # equal to the number of people in the group,
            # everyone answered yes to it
            if qDict[q] == len(group): allYes.append(q)

    # For pt. 1
    if f == 1:
        # Return how many different q entries are in dict
        return len(qDict)

    # For pt. 2
    return len(allYes)

# print(totalCount("aaZaaa", 2))
# print(totalCount(sys.stdin.read(), 2))
