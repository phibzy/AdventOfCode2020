#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 24, 2020 16:37:48 AEDT
  @file        : crabCups

"""

from pathlib import Path

# All single digits, so just
# list the string and typecast each
# element as an int
def parseInput(inp):
    return list(map(int, list(inp.strip())))

def playGame(inp, numMoves):
    # Run the damn function for
    # however many moves!
    for i in range(numMoves):
        inp = moveCups(inp.copy(), i)

    # Find cup 1 then print order of labels clockwise
    index1 = inp.index(1)
    # print(f"index1: {index1}, inp: {inp}")
    return inp[index1+1:] + inp[:index1]


# In hindsight, swaps in place were definitely
# the better way to go haha
def moveCups(inp, i):
    MOVE_CUPS = 3
    MAX = 9
    MIN = 1
    # print(f"starting inp: {inp}")
    # print("".rjust(30, "~"))

    # Mod move number to get correct
    # start index
    i = i % len(inp)
    curr    = inp[i]
    nextVal = curr - 1

    # Get slice of cups
    # and remove them from list too
    # Add extra 1 for end cups due to slice indexing
    start = i + 1
    end   = i + MOVE_CUPS + 1

    removedCups = inp[start:end]
    # bef, aft    = len(inp[:start]) + len(inp[end:])
    inp         = inp[:start] + inp[end:]

    # print(f"inp: {inp}")
    # print(f"removedCups: {removedCups}")

    # handle wrap around if need be
    end = end % MAX
    if end < start:
        removedCups += inp[:end]
        inp          = inp[end:]

    # print(f"inp: {inp}")
    # print(f"removedCups: {removedCups}")

    # Make sure dest cup isn't
    # in the slice we just took out
    if nextVal == 0: nextVal = MAX
    while nextVal in removedCups:
        # print(f"nextVal: {nextVal}")
        nextVal -= 1
        # Remember to wrap value around
        # if we go below 1
        if nextVal < MIN: nextVal = MAX

    # print(f"nextVal is {nextVal}")

    # New list is smaller so make sure
    # to subtract the number of cups moved out from mod value
    x = start % (MAX - MOVE_CUPS)
    while True:
        if inp[x] == nextVal:
            break
      
        # Wrap the index around if
        # we go past the end
        x = (x + 1) % MAX - MOVE_CUPS


    # print(f"x is {x}")

    # Insert the removed cups back where they belong
    inp = inp[:x+1] + removedCups + inp[x+1:]

    # Then rotate so original i index is preserved
    currI = inp.index(curr)
    if currI != i:
        diff = currI - i
        inp = inp[diff:] + inp[:diff]

    # Then return the new list
    return inp


inp = parseInput(Path("./input/puzzle_input").read_text())

# Pt. 1
print(playGame(inp, 100))
