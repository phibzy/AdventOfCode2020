#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Dec 07, 2020 18:05:29 AEDT
  @file        : haversacks

"""

import sys, re

#DFS time

# bag descriptions are three words
# match on {2}w bags, turn 2w into camelcase
# split on "contain"
# be careful of bag/bags case
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
    for line in inp:
        parseLine(line, bags)

    return bags

#
def DFS(bags):
    pass

print(parseLine("vibrant bronze bags contain no other bags.", dict()))
# bags = parseInput(sys.stdin.read())
