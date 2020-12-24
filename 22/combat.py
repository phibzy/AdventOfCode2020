#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 24, 2020 11:01:53 AEDT
  @file        : combat

"""

# Will use a deque to implement this

from collections import deque
from pathlib import Path

def parseInput(inp):
    # Split on blank line to separate players
    p1, p2 = inp.strip().split("\n\n")

    # Ignore first line with player name,
    # just grab the numbers for the deck
    # Reverse the list once we have it and turn it into deqeue, so popping top of deck/putting on bottom is a bit more intuitive
    p1Deck = deque(map(int, p1.strip().split("\n")[1:][::-1]))
    p2Deck = deque(map(int, p2.strip().split("\n")[1:][::-1]))

    # Return our decks
    return (p1Deck, p2Deck)

def findResult(p1d, p2d):
    # So my tests don't get upset
    p1Deck = p1d.copy()
    p2Deck = p2d.copy()

    # Keep looping until one of the decks is empty
    while p1Deck and p2Deck:
        # Draw cards from each deck
        p1Card, p2Card = p1Deck.pop(), p2Deck.pop()

        # If p1's card is greater, put both cards on bottom
        # of deck with p1 card on top of the other
        if p1Card > p2Card:
            p1Deck.appendleft(p1Card)
            p1Deck.appendleft(p2Card)

        # If p2's card is greater, put both cards on bottom
        # of deck with p2 card on top of the other
        else:
            p2Deck.appendleft(p2Card)
            p2Deck.appendleft(p1Card)

    winningDeck = p1Deck or p2Deck

    result = 0
    for num, i in zip(winningDeck, range(1, len(winningDeck) + 1)):
        result += i*num

    return result

# While p1Deck and p2Deck

inp = parseInput(Path("./input/puzzle_input").read_text()) 

# Pt.1
print(findResult(*inp))

