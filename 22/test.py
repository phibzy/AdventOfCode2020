#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from combat import parseInput, findResult
from collections import deque

class testCombat(unittest.TestCase):

    testInput = [ parseInput(f.read_text()) for f in sorted(Path("./input/").glob("test*")) ]

    def testParse(self):
        self.assertEqual(self.testInput[0], (deque([1,3,6,2,9]),
                                             deque([10,7,4,8,5])))

    def testFindResult(self):
        self.assertEqual(findResult(*self.testInput[0]), 306) 
