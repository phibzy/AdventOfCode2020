#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Wednesday Dec 02, 2020 18:23:50 AEDT
  @file        : validPass

"""

import sys

# TC: O(N) - Worst case, does have early exit though
def validPass(freq, char, pw):
    charCount = 0

    # If the current char is the target char,
    # increase the count
    for i in pw:
        if i == char:
            charCount += 1

            # Don't need to keep going if we blow past
            # the higher bound
            if charCount > freq[1]: return False

    # Check lower bound at end
    return charCount >= freq[0]

# This one deals with 1 indexes
# TC: O(1) - Takes constant time to access index of list
def validPassPt2(r, char, pw):
    # We know i2 >= i1 since in the previous part they
    # were valid ranges. So if the end index is greater
    # than the length of the password, it's impossible
    if r[1] > len(pw): return False

    # Just to make things nicer
    r[0], r[1] = r[0] - 1, r[1] - 1

    # Use XOR to check condition
    # I.e. either can be true, but not both of them
    return (pw[r[0]] == char) ^ (pw[r[1]] == char)

def parseLine(s):
    # split on colon
    # split LHS on space
    # split LLHS on '-'
    # remove first space char in RHS
    lhs, pw = s.split(":")
    rng, char = lhs.split()
    rng = list(map(int, rng.split("-")))

    return (rng, char, pw[1:])

def parseInput(inp):
    validCount = 0
 
    # Parse each line, check if it's a password
    # Increment count if it is valid
    for line in inp:
        freqRange, char, pw = parseLine(line)

        # if validPass(freqRange, char, pw):
        if validPassPt2(freqRange, char, pw):
            validCount += 1

    return validCount

# Do it this way for the sake of easy testing
inp = list()

for line in sys.stdin:
    inp.append(line.strip())

print(parseInput(inp))
