#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from pathlib import Path
from translation import parseInput, isValid, getErrorRate, getErrorRateN
from translation import validTix, pt2, trimSets, topoSort

class test(unittest.TestCase):

    testPath = Path('./input/')
    testInput = [ parseInput(f.read_text()) for f in sorted(testPath.glob("test*")) ]
    puzzleInput = parseInput(Path(testPath / 'puzzle_input').read_text())

    def testParse(self):
        self.assertEqual(self.testInput[0], ({'class': [[1,3],[5,7]], 'row': [[6,11],[33,44]],
            "seat": [[13,40],[45,50]]}, [1,40], [5,50], [7,1,14], [[7,3,47],[40,4,50],[55,2,20],[38,6,12]]))

    def testIsValid(self):
        self.assertTrue(isValid([23,40], [530,625], 23))
        self.assertTrue(isValid([23,40], [530,625], 28))
        self.assertTrue(isValid([23,40], [530,625], 40))
        self.assertTrue(isValid([23,40], [530,625], 530))
        self.assertTrue(isValid([23,40], [530,625], 625))
        self.assertTrue(isValid([23,40], [530,625], 589))

        self.assertFalse(isValid([23,40], [530,625], 12))
        self.assertFalse(isValid([23,40], [530,625], 50))
        self.assertFalse(isValid([23,40], [530,625], 670))

    def testErrorRateN(self):
        self.assertEqual(getErrorRateN(self.testInput[0][0], self.testInput[0][-1]), 71)

    # Test we get the same result with both versions
    def testErrorRate(self):
        self.assertEqual(getErrorRate(self.puzzleInput[1:3], self.puzzleInput[-1]), getErrorRateN(self.puzzleInput[0], self.puzzleInput[-1]))

    def testValidTix(self):
        self.assertEqual(validTix(self.testInput[0][0], self.testInput[0][-1]), [[7,3,47]])
        self.assertEqual(validTix(self.testInput[1][0], self.testInput[1][-1]), [[3,9,18],[15,1,5],[5,14,9]])

    def testTrim(self):
        fields = self.testInput[0][0]
        myTicket = self.testInput[0][3]
        fields2 = {"class": [[0,1],[4,19]], "row": [[0,5],[8,19]], "seat": [[0,13],[16,19]]}

        self.assertEqual(trimSets(fields, { x: set(fields.keys()) for x in range(len(myTicket)) }, [[7,1,14],[7,3,47]]), { 0: {"class", "row"}, 1: {"class"}, 2: {"seat"} })
        self.assertEqual(trimSets(fields2, { x: set(fields2.keys()) for x in range(len(myTicket)) }, [[11,12,13],[3,9,18],[15,1,5],[5,14,9]]), { 0: {"row"}, 1: {"class", "row"}, 2: {"class", "row", "seat"} })
        
    def topoSort(self):
        self.assertEqual(topoSort({ 0: {"row"}, 1: {"class", "row"}, 2: {"class", "row", "seat"} }), {"row": 0,
            "class": 1, "seat": 2})
        self.assertEqual(topoSort({ 0: {"class", "row"}, 1: {"class"}, 2: {"seat"} }), {"row": 0,
            "class": 1, "seat": 2})
