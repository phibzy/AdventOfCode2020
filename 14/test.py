#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from docking import parseInput, sumMemory, sumPt2, genCombos
from pathlib import Path

class testDocking(unittest.TestCase):

    inputPath = Path('./input/')
    testData = [ parseInput(f.read_text()) for f in sorted(inputPath.glob("test*")) ]

    def testParse(self):
        self.assertEqual(self.testData[0], [["111111111111111111111111111110111101" ,int("1000000" , 2), int("111111111111111111111111111111111101", 2), [[8, 11], [7, 101], [8, 0]]]])
    
    def testSumMemory(self):
        self.assertEqual(sumMemory(self.testData[0]), 165)

    def testSumPt2(self):
        self.assertEqual(sumPt2(self.testData[1]), 208)

    def testGenCombo(self):
        self.assertEqual(sorted(genCombos([64, 102])), [64, 102, 166])
        self.assertEqual(sorted(genCombos([1, 7, 10])), sorted([1,7,10,8,11,17,18]))
        self.assertEqual(sorted(genCombos([1, 32])), sorted([1, 32, 33]))
