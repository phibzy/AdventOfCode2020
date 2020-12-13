#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from rainRisk import parseInput, manhattanDistance

class testRain(unittest.TestCase):

    path = Path("./input/")
    testFiles = [ x.read_text() for x in sorted(path.glob("test*")) ]
    parsedFiles = list(map(parseInput, testFiles))

    def testParseInput(self):
        self.assertEqual(parseInput(self.testFiles[0]), [["F", 10], ["N", 3], ["F", 7], ["R", 90], ["F", 11]])
        self.assertEqual(self.parsedFiles[0], [["F", 10], ["N", 3], ["F", 7], ["R", 90], ["F", 11]])

    def testManhattan(self):
        self.assertEqual(manhattanDistance(self.parsedFiles[0]), 25)

