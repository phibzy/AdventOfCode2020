#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from docking import parseInput
from pathlib import Path

class testDocking(unittest.TestCase):

    inputPath = Path('./input/')
    testData = [ parseInput(f.read_text()) for f in sorted(inputPath.glob("test*")) ]

    def testParse(self):
        self.assertEqual(self.testData[0], [[int("111111111111111111111111111111111101" , 2), [[8, 11], [7, 101], [8, 0]]]])
