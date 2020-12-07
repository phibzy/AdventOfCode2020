#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Dec 07, 2020 18:05:29 AEDT
  @file        : haversacks

"""

import sys, re

# DFS time

# bag descriptions are two words followed by bag(s)
def parseLine(line, bags):
    # split on ' contain '
    # want to grab bag which is subject of rule,
    # then its list of rules
    subjectBag, ruleBags = line.split(" contain ") 

    # regex to get bag name
    subjectBag = ''.join(re.findall(r"^([a-z]+) ([a-z]+) ", subjectBag)[0])

    # add to bag dict if it hasn't been already
    bags.setdefault(subjectBag, dict())

    # "contain no other bags" case
    if re.match("no other bags", ruleBags): return bags

    # then add all the ruleBags as rules to subjectBag's dict
    for bag in ruleBags.split(', '):
        match = re.findall(r"^([1-9][0-9]*) ([a-z]+) ([a-z]+)", bag)[0]

        # Get the quantity as number, concatenate the two word bagName
        quantity, bagName = int(match[0]), match[1] + match[2]

        # add to dict
        bags[subjectBag][bagName] = quantity

    # So testing is easier
    return bags

def parseInput(inp):
    # dict of dicts for bag possibilities
    bags = dict()

    # Add rule to dict
    for line in inp.splitlines():
        parseLine(line, bags)

    return bags

def countPaths(bags, targetBag):
    # change the bagname to match field in dict
    targetBag = ''.join(targetBag.split())
    
    count = 0

    for bag in bags:
        if bag == targetBag: continue
        count += DFS(bags, bag, targetBag)

    return count

# DFS for target bag name
# we'll try do it iteratively for once
# return 1 if found, 0 if not
def DFS(bags, startBag, targetBag):
    # stack for DFS, visited dict to prevent cycles
    s = list()
    visited = dict()
    s.append(startBag)

    while s:
        nextBag = s.pop()

        for bag in bags[nextBag]:
            # Don't bother if we've already seen it before
            if bag in visited: continue

            # Return true if we find the target
            if bag == targetBag: return 1 

            # Otherwise keep looking
            s.append(bag)

    return 0


# We'll do this recursively because laziness
# TC: O(N) - worst every bag type is in our bag
# SC: O(N) - Same as above, resulting in N calls on stack
# Iterative method: same as above but with tuples to keep track
# of multipliers
def sumBagsR(bags, startBag):
    bagCount = 1

    # For each bag contained within our chosen bag
    for bag in bags[startBag]:
        
        # Add the amount of that bag * the number of bags
        # in their contents
        bagCount += bags[startBag][bag]*sumBagsR(bags, bag)

    return bagCount

def sumBags(bags, startBag):
    # We don't include the starting bag
    # because we're only counting how many bags
    # there are inside of it
    return sumBagsR(bags, startBag) - 1

# Create a dict with each different bag name as keys,
# with their values being a dict with bagName/quantity pairs
# bags = parseInput(sys.stdin.read())

# print(countPaths(bags, "shiny gold"))
# print(sumBags(bags, "shinygold"))

