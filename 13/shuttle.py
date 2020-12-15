#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Dec 14, 2020 16:21:40 AEDT
  @file        : shuttle

"""

from pathlib import Path

# Question: Find the lowest multiple of each number
# that is greater than or equal to earliest depart time

# Depart time will be positive number with no leading zeroes
# Second line will be comma separated numbers

def parseInput(inp):
    # Grab depart time
    departTime, busList = inp.strip().split("\n")
    departTime = int(departTime)

    # Grab list of bus numbers, leave x's there in case part 2 needs them
    busList = [ int(bus) if bus != "x" else bus for bus in busList.split(",") ]

    return (departTime, busList)

# find lowest multiple greater than or equal to target
# there is exactly one result
# Divide target by num.
# If there's no remainder then return target
# since it's a multiple and nothing will beat that.
# Otherwise, return ceiling of result * num (i.e.
# closest multiple greater than target)
def lowestMultiple(target, num):
    # condition for x's, make them infinity
    if num == "x": return float('inf')

    # divmod performs division, but separates the
    # integer and float component
    result, rem = divmod(target, num)

    # If there's a remainder, we round up and multiply
    # by num to get lowest multiple
    if rem: return (result+1)*num

    # No remainder, so target is lowest multiple
    return target

def earliestTime(target, inp):
    # find earliest time + its index
    eTs = [ (i, lowestMultiple(target, bus)) for i, bus in enumerate(inp) ]
    eT = min(eTs, key=lambda x: x[1])
    
    # Get ID of bus with earliest time
    # using the index of min element in eTs
    busID = inp[eT[0]]
    min2Wait = eT[1] - target

    # Return busID times the minutes we have to wait
    return busID*min2Wait

inp = parseInput(Path('./input/puzzle_input').read_text())
print(earliestTime(*inp))
