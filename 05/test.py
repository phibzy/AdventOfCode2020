#!/usr/bin/python3

"""
    Test Cases:
        - binSearch on cols
        - binSearch on rows
        - findSeat
"""

import unittest
from boarding import binSearch, decodeSeat, COLS, ROWS, findSeat

class testBoarding(unittest.TestCase):

    def testFindSeat(self):
        self.assertEqual(findSeat([1,2,4,5]), 3)
        self.assertEqual(findSeat([31,32,33,35,36]), 34)

    def testDecodeSeat(self):
        self.assertEqual(decodeSeat("BFFFBBFRRR"), 567)
        self.assertEqual(decodeSeat("FFFBBBFRRR"), 119)
        self.assertEqual(decodeSeat("BBFFBBFRLL"), 820)
        self.assertEqual(decodeSeat("FBFBBFFRLR"), 357)

    def testBinSearchRow(self):
        self.assertEqual(binSearch("FBFBBFF", ROWS), 44)
        self.assertEqual(binSearch("BFFFBBF", ROWS), 70)
        self.assertEqual(binSearch("FFFBBBF", ROWS), 14)
        self.assertEqual(binSearch("BBFFBBF", ROWS), 102)


    def testBinSearchCol(self):
        self.assertEqual(binSearch("RLR", COLS), 5)
        self.assertEqual(binSearch("RRR", COLS), 7)
        self.assertEqual(binSearch("RLL", COLS), 4)
        self.assertEqual(binSearch("LLL", COLS), 0)
        self.assertEqual(binSearch("RRL", COLS), 6)
