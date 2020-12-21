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

        # Sum the results of each line together
        total += evalLine(line)

    return total

def evaluate2(inp):
    total = 0

    # print(inp)

    # Evaluate each line in input
    for line in inp.strip().split("\n"):
        # Get rid of spaces
        line = re.sub(' ', '', line)

        # Sum the results of each line together
        total += evalLine2(line)

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
            if lastOp:
                # If there's a lastOp, there must be a lastVal
                currTotal = opF[lastOp.pop()](lastVal.pop(), currTotal)

        # If it's an operator, set our current operator
        # Can get away with this since we'll never have "+*" etc.
        elif char in opF:
            currOp = char

        # Otherwise it's a number
        # Convert it to an int and then apply our current operator
        else:
            num = 0
            while i < len(line) and line[i].isdigit():
                num = num * 10 + int(line[i])
                i += 1
            
            # continue here since we don't want to over increment
            # our pointer
            currTotal = opF[currOp](currTotal, num)
            continue
        
        i += 1

    return currTotal

# Function for evalutating each line
def evalLine2(line):
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

    # Create extra stack for '*' operator
    mStack = list()
    flagStack = list()
    mFlag = False

    # Go char by char
    i = 0
    while i < len(line):
        print("".rjust(30, "#"))
        print(currTotal)
        char = line[i]
        # print(char)

        # Bracket expression, so store what we have on stack
        if char == "(":
            lastVal.append(currTotal)
            lastOp.append(currOp)
            flagStack.append(mFlag)

            # Reset these in case our lastOp was *
            currTotal, currOp = 0, "+"
            mFlag = False

        # Bracket expression ends, unwind the stack 1 step
        elif char == ")":
            # Be careful of case where there's nothing before
            # bracket expression
            if lastOp:
                # If there's a lastOp, there must be a lastVal
                currLop = lastOp.pop()
                currLv = lastVal.pop()
                if flagStack: mFlag = flagStack.pop()

                if currLop == "*":
                    mStack.append(currLv)

                else:
                    currTotal = opF[currLop](currLv, currTotal)

        # If it's an operator, set our current operator
        # Can get away with this since we'll never have "+*" etc.
        elif char in opF:
            currOp = char

            # Can evaluate previous mulitply op
            # if there's nothing with higher precedence
            if char == "*" and mStack and mFlag:
                currTotal *= mStack.pop()

        # Otherwise it's a number
        # Convert it to an int and then apply our current operator
        else:
            print("".rjust(30, "~"))
            num = 0
            while i < len(line) and line[i].isdigit():
                num = num * 10 + int(line[i])
                i += 1

            print(f"currOp: {currOp}, currTotal: {currTotal}, num: {num}")

            # Pt. 2:
            # Only thing we need to handle differently is +/* ops
            # Don't evaluate immediately if it's a * sign, keep track
            # of current total on stack
            if currOp == "*":
                mStack.append(currTotal)
                currTotal = num
                mFlag = True

            else:
                currTotal = opF[currOp](currTotal, num)

            # continue here since we don't want to over increment
            # our pointer
            continue
        
        i += 1

    while mStack:
        currTotal *= mStack.pop()

    return currTotal

inp = Path("./input/puzzle_input").read_text()

# Pt. 1
# print(evaluate(inp))

# Pt. 2
# print(evaluate2(inp))
print(evaluate2("2*3 + (4*5)"))
