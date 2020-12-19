#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from pt2 import parseInput, cycle, runCycles

class testPt2(unittest.TestCase):

    testInput = [ parseInput(f.read_text()) for f in sorted(Path('./input/').glob("test*")) ]

    def testCycle(self):
        self.assertEqual(cycle(self.testInput[0])[1], 29)

    def testRunCycles(self):
        self.assertEqual(runCycles(self.testInput[0], 2), 60)
        self.assertEqual(runCycles(self.testInput[0], 6), 848)
