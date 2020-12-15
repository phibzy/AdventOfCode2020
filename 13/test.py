#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from shuttle import parseInput, lowestMultiple, earliestTime

class testShuttle(unittest.TestCase):

    testPath = Path("./input/")
    testInput = list(map(parseInput, [f.read_text() for f in sorted(testPath.glob("test*"))]))

    def testParse(self):
        self.assertEqual(self.testInput[0], (939, [7,13,"x","x",59,"x",31,19]))

    def testLowestMultiple(self):
        self.assertEqual(lowestMultiple(939, 1), 939)
        self.assertEqual(lowestMultiple(939, 7), 945)
        self.assertEqual(lowestMultiple(939, 59), 944)
        self.assertEqual(lowestMultiple(939, "x"), float('inf'))

    def testEarliestTime(self):
        self.assertEqual(earliestTime(*self.testInput[0]), 295)
