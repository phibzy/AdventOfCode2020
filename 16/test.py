#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from translation import parseInput

class test(unittest.TestCase):

    testPath = Path('./input/')
    testInput = [ parseInput(f.read_text()) for f in sorted(testPath.glob("test*")) ]

    def testParse(self):
        self.assertEqual(self.testInput[0], ({'class': [[1,3],[5,7]], 'row': [[6,11],[33,44]],
            "seat": [[13,40],[45,50]]}, [1,40], [5,50], [7,1,14], [[7,3,47],[40,4,50],[55,2,20],[38,6,12]]))
