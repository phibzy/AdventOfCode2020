#!/usr/bin/python3

"""
    Test Cases:
        - Default cases
        - No brackets
        - Multi-digit numbers in input

"""

import unittest
from pathlib import Path
from operations import evaluate, evaluate2

class testOps(unittest.TestCase):

    testPath = Path('./input/')
    testInput = [ f.read_text() for f in sorted(testPath.glob("test*")) ]

    def testEvaluate(self):
        self.assertEqual(evaluate(self.testInput[0]), 26)
        self.assertEqual(evaluate(self.testInput[1]), 437)
        self.assertEqual(evaluate(self.testInput[2]), 12240)
        self.assertEqual(evaluate(self.testInput[3]), 13632)
        self.assertEqual(evaluate(self.testInput[4]), 26335)
        self.assertEqual(evaluate(self.testInput[5]), 90)
        self.assertEqual(evaluate(self.testInput[6]), 588968)
        self.assertEqual(evaluate(self.testInput[7]), 1046)
        self.assertEqual(evaluate(self.testInput[8]), 62673715200)
        self.assertEqual(evaluate(self.testInput[9]), 1000)

    def testEvaluate2(self):
        self.assertEqual(evaluate2(self.testInput[0]), 46)
        self.assertEqual(evaluate2(self.testInput[1]), 1445)
        self.assertEqual(evaluate2(self.testInput[2]), 669060)
        self.assertEqual(evaluate2(self.testInput[3]), 23340)
