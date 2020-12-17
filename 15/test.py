#!/usr/bin/python3

import unittest
from pathlib import Path
from recitation import numberSpoken

class testRecitation(unittest.TestCase):

    # Create lists for test input
    testInput = [ list(map(int, f.read_text().split(','))) for f in sorted(Path("./input/").glob("test*")) ]  

    def testNumberSpoken(self):
        # Target is 2020th number for each test
        target = 2020

        self.assertEqual(numberSpoken([1,2,3], 6), 1)

        self.assertEqual(numberSpoken(self.testInput[0], target), 436)
        self.assertEqual(numberSpoken(self.testInput[1], target), 1)
        self.assertEqual(numberSpoken(self.testInput[2], target), 10)
        self.assertEqual(numberSpoken(self.testInput[3], target), 27)
        self.assertEqual(numberSpoken(self.testInput[4], target), 78)
        self.assertEqual(numberSpoken(self.testInput[5], target), 438)
        self.assertEqual(numberSpoken(self.testInput[6], target), 1836)

        # Testing pt. 2 target
        target = 30000000

        self.assertEqual(numberSpoken(self.testInput[0], target), 175594)
        self.assertEqual(numberSpoken(self.testInput[1], target), 2578)
        self.assertEqual(numberSpoken(self.testInput[2], target), 3544142)
        self.assertEqual(numberSpoken(self.testInput[3], target), 261214)
        self.assertEqual(numberSpoken(self.testInput[4], target), 6895259)
        self.assertEqual(numberSpoken(self.testInput[5], target), 18)
        self.assertEqual(numberSpoken(self.testInput[6], target), 362)
