#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from shuttle import parseInput

class testShuttle(unittest.TestCase):

    testPath = Path("./input/")
    testInput = list(map(parseInput, [f.read_text() for f in sorted(testPath.glob("test*"))]))

    def testParse(self):
        self.assertEqual(self.testInput[0], (939, [7,13,"x","x",59,"x",31,19]))

