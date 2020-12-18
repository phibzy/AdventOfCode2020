#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 17, 2020 14:24:57 AEDT
  @file        : translation

"""

import re
from pathlib import Path
from collections import deque

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
    
    # Since each field has two groups
    # We'll get the full range of values for each group
    group1R = [float('inf'), 0]
    group2R = [float('inf'), 0]

    fieldRules = dict()
    for line in rules.split("\n"):
        # Grab name of field, and the 2 endpoints of both ranges
        field, range1s, range1e, range2s, range2e = re.findall("^(.*): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)$", line)[0]
        fieldRules[field] = [[int(range1s), int(range1e)], [int(range2s), int(range2e)]]

        # Since all ranges of fields overlap in puzzle input,
        # we can just compare mins/maxes of ranges
        group1R = [min(group1R[0], int(range1s)), max(group1R[1], int(range1e)) ]
        group2R = [min(group2R[0], int(range2s)), max(group2R[1], int(range2e)) ]

    # For the next group, ignore the "your ticket" text
    # and split the next line at commas and place into a list
    # Then convert each element into an int
    myVals = list(map(int, yourTix.split("\n")[1].split(",")))

    # Similarly here we can ignore "nearby tickets"
    # and do the same process for each other ticket,
    # creating a list of all other ticket data
    otherTix = otherTix.strip().split("\n")[1:]
    for i in range(len(otherTix)):
        otherTix[i] = list(map(int, otherTix[i].split(",")))

    return (fieldRules, group1R, group2R, myVals, otherTix)

# Check if a value is valid
def isValid(range1, range2, val):
    return (range1[0] <= val <= range1[1]) or (range2[0] <= val <= range2[1])

############### Pt. 1 ######################

# For puzzle input
def getErrorRate(ranges, tickets):
    errorRate = 0

    # Since we have two giant ranges to check for our puzzle
    # input, we don't need to go through every field checking
    # their individual ranges
    for ticket in tickets:
        for val in ticket:

            if not isValid(*ranges, val):
                errorRate += val

    return errorRate 

# For all other input
def getErrorRateN(fields, tickets):
    errorRate = 0

    for ticket in tickets:
        for val in ticket:
            valid = False
            for field in fields.values():
                # print(field)

                if isValid(*field,val):
                
                    valid = True
                    break

            if not valid: errorRate += val

    return errorRate

############### Pt. 2 #######################

# For this one, we're going to be using indices
# Start by making a dict of sets for each field index
# Each column index will map to a set of each valid field description
# Since we will have cases where we'll need deduction to work out
# valid field mappings, we want to find all valid fields for a column
# We'll pass through each ticket, removing possibilities for a field
# every time there's an invalid check

# For this to work though we first need to remove all invalid tickets

# We're then going to start with the sets with least elements, work 
# out their field, then remove said field from the other sets
# to narrow down possibilities. Rince and repeat until all sets
# have one element - a unique field.

# Think of it like a topological sort-like problem

# Getting rid of invalid tickets
def validTix(fields, tickets):
    tikNum = 0

    # While since we're deleting as we go
    while tikNum < len(tickets):

        for val in tickets[tikNum]:
            valid = False

            for field in fields.values():

                # Confirmed valid, don't need to check further
                if isValid(*field,val):
                    valid = True
                    break

            if not valid: break

        # Remove a ticket if it's invalid
        # increment the count otherwise
        if valid: tikNum += 1
        else: del tickets[tikNum]

    return tickets

def trimSets(fieldInfo, pSets, tickets):
    # Check each column, remove all fields its set that aren't valid
    for col in range(len(tickets[0])):

        for row in range(len(tickets)):

            # If invalid result, remove the field possibility
            # for that column
            for field in fieldInfo:
                ranges = fieldInfo[field]
                
                if not isValid(*ranges, tickets[row][col]) and field in pSets[col]:
                    pSets[col].remove(field)

    return pSets

def pt2(inp):
    # We don't need the all encompassing ranges we used before
    fieldInfo, _, _, myTicket, otherTickets = inp

    pSets = { x: set(fieldInfo.keys()) for x in range(len(myTicket)) }

    # Get rid of all invalid tickets first up
    # Then include our own ticket in deduction process
    tickets = validTix(fieldInfo, otherTickets) + [ myTicket ]

    # Trim our pSets as well
    pSets = trimSets(fieldInfo, pSets, tickets)

    # Topological sort time
    fieldMapping = topoSort(pSets)

    # We have column mappings, now we'll find every field starting
    # with 'departure' and multiply them together
    currentProduct = 1

    # If the field matches, get the columnIndex it
    # maps to. Then multiply with current product
    for field in fieldMapping:
        if re.match("^departure", field):
            currentProduct *= myTicket[fieldMapping[field]]

    return currentProduct


def topoSort(pSets):
    field2Col = dict()
    # Create a queue of all indices with set length 1
    # I.e. those columns with only one possibility for their field
    while pSets:
        q = deque()

        for i in pSets:
            # Append to q if set length is 1
            if len(pSets[i]) == 1:
                q.append(i)

        # Process the q
        while q:
            # Gets the only element in set by abusing unpacking lol
            colIndex = q.pop()
            nextField,  = pSets[colIndex]

            # Remove this field from all the other sets
            for s in pSets.values():
                if nextField in s:
                    s.remove(nextField)

            # Keep track of field -> index mapping, 
            # then remove column from pSets
            field2Col[nextField] = colIndex
            del pSets[colIndex]

    return field2Col

inp = parseInput(Path('./input/puzzle_input').read_text())

# Pt. 1
# print(getErrorRate(inp[1:3], inp[-1]))

# Although this may get the correct answers,
# there's a lot of unuaccounted for edge cases.
# E.g. the definition of a valid ticket is one
# where each field is valid for some field definition.
# But what this doesn't account for is if more than one
# field is valid for only a single definition, yet
# it's the same one as another field with a single
# valid definition.

# My part 2 solution also assumes there is at least
# one column at the start which only has one possible
# field.

# Pt. 2
print(pt2(inp))
