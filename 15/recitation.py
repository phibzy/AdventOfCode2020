#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Thursday Dec 17, 2020 10:41:01 AEDT
  @file        : recitation

"""

puzzleInput = [0,14,1,3,7,9]
# Have a dict of numbers, which keeps track of 1 indexes

# Assuming based on input that starting numbers are unique
def numberSpoken(inp, target):
    # Dict keeping track of spoken numbers
    spoken = dict()

    # Count keeping track of turns
    turn = 1

    for num in inp:
        spoken[num] = turn
        turn += 1

    # Since input numbers are all unique
    lastNum = 0

    while True:
        # If we reach our target turn, returnt the current number
        if turn == target: return lastNum

        # if the current number has been spoken before,
        # our next spoken number is the difference between
        # the current turn and the last turn the current number
        # had been seen.
        if lastNum in spoken:
            diff, spoken[lastNum] = turn - spoken[lastNum], turn
            lastNum = diff

            # this didn't work for some reason, dunno why - maybe due to dict mutability?
            # lastNum, spoken[lastNum] = (turn - spoken[lastNum]), turn

        # Otherwise the next number is 0, we also
        # update the dict keeping track of the last turn
        # current number was spoken
        else:
            spoken[lastNum] = turn
            lastNum = 0

        turn += 1

# Pt. 1
# print(numberSpoken(puzzleInput, 2020))

# Pt. 2
print(numberSpoken(puzzleInput, 30000000))
