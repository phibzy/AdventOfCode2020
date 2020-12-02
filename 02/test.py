#!/usr/bin/python3

"""
    Test Cases:


"""

import unittest
from validPass import parseInput, parseLine, validPass, validPassPt2

class testValidPass(unittest.TestCase):

    def testParseLine(self):
        self.assertEqual(parseLine("10-11 q: kqqqzqqfqqqqq"), ([10,11], "q", "kqqqzqqfqqqqq"))
        self.assertEqual(parseLine("3-4 n: znnn"), ([3,4], "n", "znnn"))
        self.assertEqual(parseLine("3-13 w: plwqwhbwdgxcwfmwjl"), ([3,13], "w", "plwqwhbwdgxcwfmwjl"))
        self.assertEqual(parseLine("1-3 z: mzzh"), ([1,3], "z", "mzzh"))

    def testVP(self):
        self.assertTrue(validPass([1,3], "z", "mzzh"))
        self.assertFalse(validPass([12,13], "v", "vvvvvvvvvvvvvv"))
        # TIL: * operator on tuples/lists unpacks them into arguments
        self.assertTrue(validPass(*parseLine("6-7 w: wkjwwwnmww")))
        self.assertFalse(validPass(*parseLine("6-7 w: wkjnmww")))

    def testVPPt2(self):
        self.assertTrue(validPassPt2(*parseLine("6-7 w: wkjwwwnmww")))


