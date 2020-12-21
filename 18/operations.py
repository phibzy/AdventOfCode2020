#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Dec 20, 2020 12:18:28 AEDT
  @file        : operations

"""

from pathlib import Path
from operator import mul, add
import re

# Basic algo:
# For each line
# Go through input char by char (remove spaces first)
# if number convert to int


def evaluate(inp):
    total = 0

    # print(inp)

    # Evaluate each line in input
    for line in inp.strip().split("\n"):
        # Get rid of spaces
        line = re.sub(' ', '', line)

        # out all empty strings
        # line = list(filter(None, line))
        # line = list(filter(None, re.split(r"[\(\)]", line)))

        # Sum the results of each line together
        total += evalLine(line)

    return total

# Function for evalutating each line
def evalLine(line):
    # print(line)
    # print("".rjust(30, "~"))
    # Map the symbols to the right function call
    opF = {"+": add, "*": mul}

    # Start off with these
    # We're only dealing with positive stuff after all
    currTotal = 0
    currOp    = "+"

    # Use stacks to keep track of operators/vals 
    lastVal = list()
    lastOp = list() 

    # Algo:
    # if we come across an open bracket, place
    # last operator/current val on stack

    # When we come across a closed bracket, unwind stack
    # one step since we now have the latest bracket expression
    # evaluated. We then evaluate lastVal 'lastOp' currentTotal. 

    # Go char by char
    i = 0
    while i < len(line):
        char = line[i]
        # print(char)

        # Bracket expression, so store what we have on stack
        if char == "(":
            lastVal.append(currTotal)
            lastOp.append(currOp)

            # Reset these in case our lastOp was *
            currTotal, currOp = 0, "+"

        # Bracket expression ends, unwind the stack 1 step
        elif char == ")":
            # Be careful of case where there's nothing before
            # bracket expression
            # print()
            # print(f"Before: {currTotal}")
            if lastOp:
                # If there's a lastOp, there must be a lastVal
                currTotal = opF[lastOp.pop()](lastVal.pop(), currTotal)
            # print(f"After: {currTotal}")
            # print()

        # If it's an operator, set our current operator
        # Can get away with this since we'll never have "+*" etc.
        elif char in opF:
            currOp = char

        # Otherwise it's a number
        # Convert it to and int and then apply our current operator
        else:
            num = 0
            while i < len(line) and line[i].isdigit():
                num = num * 10 + int(line[i])
                i += 1

            currTotal = opF[currOp](currTotal, num)
            continue
        
        i += 1

    return currTotal

inp = Path("./input/puzzle_input").read_text()
print(evaluate(inp))
# print(evaluate("1 + 2 * 3 + 4 * 5 + 6"))
# print(evaluate("(20 * ((2 * 3) + (4 * (5 + 6))))"))

