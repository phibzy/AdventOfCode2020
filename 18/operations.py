#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Sunday Dec 20, 2020 12:18:28 AEDT
  @file        : operations

"""

from pathlib import Path
import re


# Basic algo:
# For each line
# Go through input char by char (remove spaces first)
# if number convert to int


# Cases: multi-digit numbers

def evaluate(inp):
    total = 0

    for line in inp.strip():
        total += evalLine(line)

    return total


def evalLine(inp, i):
    pass
