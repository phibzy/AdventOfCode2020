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

    # WinningDeck is whichever one of the two
    # still has cards in it
    winningDeck = p1Deck or p2Deck

    # Loop through each item in winning deck,
    # multiplying it by its 1-index
    result = 0
    for i, num in enumerate(winningDeck): 
        result += (i+1)*num

    return result

# Checks to see who wins a given round
# Returns 1 if player 1 wins, 2 if player 2 wins
def pt2(p1d, p2d, firstCall):
    # So my tests don't get upset
    # This also preserves isolation of slices
    p1Deck = p1d.copy()
    p2Deck = p2d.copy()

    history = dict()

    # Keep looping until one of the decks is empty
    while p1Deck and p2Deck:
        # Convert decks to strings since they're
        # unhashable types

        # If we've seen this exact situation before,
        # player 1 wins
        if str((p1Deck, p2Deck)) in history:
            p2Deck = []
            break

        # Add current state to history
        history[str((p1Deck, p2Deck))] = 1

        # Draw cards from each deck
        p1Card, p2Card = p1Deck.pop(), p2Deck.pop()

        # Play a recursive game of
        # recursive combat if there are at least 
        # X amount of cards in each deck, where X
        # is the value each drawn card for this turn
        if len(p1Deck) >= p1Card and len(p2Deck) >= p2Card:
            # Have to be hacky since deques don't support slices
            # But basically, convert to list, then take next
            # X amount of cards, then convert back to deque
            # so subcall works
            nextP1d = deque(list(p1Deck)[-p1Card:])
            nextP2d = deque(list(p2Deck)[-p2Card:])
            result = pt2(nextP1d, nextP2d, 0)

        # Otherwise, use same rules as before
        # and compare cards
        else:
            result = (p1Card > p2Card)

        # If p1 won the round, do the same as before
        # with cards on bottom of p1 deck
        if result == 1:
            p1Deck.appendleft(p1Card)
            p1Deck.appendleft(p2Card)

        # Same thing for p2 deck if p2 won
        else:
            p2Deck.appendleft(p2Card)
            p2Deck.appendleft(p1Card)

    # WinningDeck is whichever one of the two
    # still has cards in it
    winningDeck = p1Deck or p2Deck

    # If original call, do the result calculation
    if firstCall:
        # Loop through each item in winning deck,
        # multiplying it by its 1-index
        result = 0
        for i, num in enumerate(winningDeck): 
            result += (i+1)*num

        return result

    # Otherwise just return which player won
    if p1Deck: return 1
    if p2Deck: return 2

inp = parseInput(Path("./input/puzzle_input").read_text()) 

# Pt.1
print(findResult(*inp))

# Pt. 2
print(pt2(*inp, 1))

