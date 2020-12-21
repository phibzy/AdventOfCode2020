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

    # Evaluate each line in input
    for line in inp.strip().split("\n"):
        # Get rid of spaces
        line = re.sub(' ', '', line)

        # Split line on brackets and filter
        # out all empty strings
        line = list(filter(None, re.split(r"[\(\)]", line)))

        # Sum the results of each line together
        total += evalLine(line)

    return total

def evalLine(line):
    # Map the symbols to the right function call
    opF = {"+": add, "*": mul}

    total = None

    # Use stacks to keep track of operators/vals 
    lastVal = list()
    lastOp = list()

    # For each bracket separated expression
    for exp in line:
        curr = 0

        # Separate out numbers and operators
        nums = list(map(int, re.findall("[0-9]+", exp)))
        ops  = re.findall("[\+\*]", exp)

        # Check if we start with operator or not
        # if we do, put it on stack update ops list
        if exp[0] in ops:
            lastOp.append(exp[0])
            ops = ops[1:]

        # Otherwise we start with a number
        # so trim it off start of number list
        else:
            curr = nums[0]
            nums = nums[1:]
        
        for n, o in zip(nums, ops):
            curr = opF[o](curr, n)

        lastVal.append(curr)    

    total = lastVal[0]

    for n, o in zip(lastVal[1:], lastOp):
        total = total[o](curr, n)

    return total

