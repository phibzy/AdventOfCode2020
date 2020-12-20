#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from operations import evaluate

class testOps(unittest.TestCase):

    testPath = Path('./input/')
    testInput = [ f.read_text() for f in sorted(testPath.glob("test*")) ]

    def testEvaluate(self):
        self.assertEqual(evaluate(self.testInput[0]), 26)
        self.assertEqual(evaluate(self.testInput[1]), 437)
        self.assertEqual(evaluate(self.testInput[2]), 12240)
        self.assertEqual(evaluate(self.testInput[3]), 13632)
        self.assertEqual(evaluate(self.testInput[4]), 26335)

