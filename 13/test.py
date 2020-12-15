#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from shuttle import parseInput, lowestMultiple, earliestTime
from shuttle import earliestOffsetTime

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

    def testEarliestOffsetTime(self):
        self.assertEqual(earliestOffsetTime([17, "x", 13, 19]), 3417)
        self.assertEqual(earliestOffsetTime([67, 7, 59, 61]), 754018)
        self.assertEqual(earliestOffsetTime([67, "x", 7, 59, 61]), 779210)
        self.assertEqual(earliestOffsetTime([67, 7, "x", 59, 61]), 1261476)
        self.assertEqual(earliestOffsetTime([1789, 37, 47, 1889]), 1202161486)

