#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Dec 07, 2020 18:05:29 AEDT
  @file        : haversacks

"""

import sys, re

#DFS time

bags = dict()

# # dict of dicts for bag possibilities
# bags = {"lightRed": lightRed, "darkOrange": darkOrange, "brightWhite": brightWhite,
        # "mutedYellow": mutedYellow, "shinyGold": shinyGold, "darkOlive": darkOlive,
        # "vibrantPlum": vibrantPlum, "fadedBlue": fadedBlue, "dottedBlack": dottedBlack}

# # Bag rules

# lightRed = {'brightWhite': 1, "mutedYellow": 2}
# darkOrange = {'brightWhite': 3, "mutedYellow": 4}
# brightWhite = {'shinyGold': 1}
# mutedYellow = {'shinyGold': 2, "fadedBlue": 9}
# shinyGold = {'darkOlive': 1, "vibrantPlum": 2}
# darkOlive = {'fadedBlue': 3, "dottedBlack": 4}
# vibrantPlum = {'fadedBlue': 5, "dottedBlack": 6}
# fadedBlue = dict()
# dottedBlack = dict()

# Just apply above thinking but do it dynamically haha

# bag descriptions are three words
# match on {2}w bags, turn 2w into camelcase
# split on "contain"
# be careful of bag/bags case

def parseLine(line):
    # split on ' contain '
    # want to grab bag which is subject of rule,
    # then its list of rules
    subjectBag, ruleBags = line.split(" contain ") 

    # regex to get bag name
    subjectBag = ''.join(re.findall(r"^([a-z]+) ([a-z]+) ", subjectBag)[0])

    # add to bag dict if it hasn't been already
    bags.setdefault(subjectBag, dict())

    # then add all the ruleBags as rules to subjectBag's dict
    for bag in ruleBags.split(', '):
        match = re.findall(r"^([1-9][0-9]*) ([a-z]+) ([a-z]+)", bag)[0]

        # Get the quantity as number, concatenate the two word bagName
        quantity, bagName = int(match[0]), match[1] + match[2]

        # add to dict
        bags[subjectBag][bagName] = quantity

parseLine("muted tomato bags contain 1 bright brown bag, 1 dotted gold bag, 2 faded gray bags, 1 posh yellow bag.")
