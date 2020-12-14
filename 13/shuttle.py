#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Monday Dec 14, 2020 16:21:40 AEDT
  @file        : shuttle

"""

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

