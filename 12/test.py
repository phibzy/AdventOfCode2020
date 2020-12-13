#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from rainRisk import parseInput, manhattanDistance, manhattanPt2, rotatePoint

class testRain(unittest.TestCase):

    path = Path("./input/")
    testFiles = [ x.read_text() for x in sorted(path.glob("test*")) ]
    parsedFiles = list(map(parseInput, testFiles))

    def testParseInput(self):
        self.assertEqual(parseInput(self.testFiles[0]), [["F", 10], ["N", 3], ["F", 7], ["R", 90], ["F", 11]])
        self.assertEqual(self.parsedFiles[0], [["F", 10], ["N", 3], ["F", 7], ["R", 90], ["F", 11]])

    def testManhattan(self):
        self.assertEqual(manhattanDistance(self.parsedFiles[0]), 25)

        # 0 manhattan distance tests, just turning around and moving
        # forward same distance each direction
        self.assertEqual(manhattanDistance(self.parsedFiles[1]), 0)
        self.assertEqual(manhattanDistance(self.parsedFiles[2]), 0)
        self.assertEqual(manhattanDistance(self.parsedFiles[3]), 23)

    def testManhattan(self):
        self.assertEqual(manhattanPt2(self.parsedFiles[0]), 286)

    def testRotate(self):
        self.assertEqual(rotatePoint([0,4], 1, "R"), [4,0])
        self.assertEqual(rotatePoint([0,4], 2, "R"), [0,-4])
        self.assertEqual(rotatePoint([0,4], 2, "L"), [0,-4])
        self.assertEqual(rotatePoint([0,4], 3, "R"), [-4,0])
        self.assertEqual(rotatePoint([0,4], 1, "L"), [-4,0])

        
        self.assertEqual(rotatePoint([10,4], 1, "R"), [4,-10])
        self.assertEqual(rotatePoint([4, -10], 1, "R"), [-10, -4])
        self.assertEqual(rotatePoint([-10,-4], 1, "R"), [-4,10])
