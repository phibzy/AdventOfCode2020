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
    eTs = [ lowestMultiple(target, bus) for bus in inp ] 
    eT = min(eTs)
    
    # BusID of bus with earliest time will be element
    # in original input with same index as minimum of eTs
    busID = inp[eTs.index(eT)]
    min2Wait = eT - target

    # Return busID times the minutes we have to wait
    return busID*min2Wait

def earliestOffsetTime(busList):
    # Change x's into 1s, makes it way easier
    busList = [ 1 if bus == "x" else bus for bus in busList ]

    # Want to find some time t, such that:
    # t % busList[0] == 0, t + 1 % busList[1] == 0, t + 2 % busList[2] == 0...
    # all the way up to t + (n - 1) % busList[(n - 1)] == 0

    # First, find a number i such that i % x[0] == 0, i + 1 % x[1] == 0
    # Once we have these numbers, we find the LCM of x[1] and x[0]
    # The reason for this is that we can maintain the above relationship
    # with these two numbers if we increase them by the minimum number
    # that will maintain this relationsip. I.e. the smallest increment
    # that is a multiple of both numbers
    # At the start this is just the first number of the sequence
    lcm = busList[0]

    # Our starting timestamp
    curr = busList[0]

    # Count of distance from first timestamp
    count = 1
    
    # Start search from 2nd element, since first element is starting point
    for bus in busList[1:]:
        # Keep searching for timestamp where condition holds
        while ((curr + count) % bus != 0):
            # We increment timestamp by LCM, because we want to maintain our
            # existing relationships
            curr += lcm
        
        # We update LCM by multiplying with current busID
        # This means we can maintain all the existing relationships
        # while also maintaining the newly discovered one
        lcm*= bus
        count += 1
    
    # Return the timestamp
    return curr 

inp = parseInput(Path('./input/puzzle_input').read_text())

# For Pt. 1 answer
# print(earliestTime(*inp))

# For Pt. 2 answer
print(earliestOffsetTime(inp[1]))

