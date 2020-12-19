#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from pt2 import parseInput, cycle #, updateSpace, expandGrid, runCycles

class testPt2(unittest.TestCase):

    testInput = [ parseInput(f.read_text()) for f in sorted(Path('./input/').glob("test*")) ]

    def testCycle(self):
        self.assertEqual(cycle(self.testInput[0])[1], 29)

