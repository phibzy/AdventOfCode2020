#!/usr/bin/python3

"""
    Test Cases:
    
        Part 1:
            - 2020 and 0 in the list
            - Default case
            - Rando case

        Part 2:
            - Default case
            - Zero case
            - Rando case

"""

import unittest
from reportRepair import reportRepairPart1, reportRepairPart2 

class testRR(unittest.TestCase):

    def testPart1Zero(self):
        self.assertEqual(reportRepairPart1([7,30,2,2020,0], 2020), 0)

    def testPart1Default(self):
        self.assertEqual(reportRepairPart1([1721,979,366,299,675,1456], 2020), 514579)

    def testPart2Zero(self):
        self.assertEqual(reportRepairPart2([7,30,0,2,2020,0]), 0)

    def testPart2One(self):
        self.assertEqual(reportRepairPart2([7,30,1,2,2018,1]), 2018)

    def testPart2Default(self):
        self.assertEqual(reportRepairPart2([1721,979,366,299,675,1456]), 241861950)

    def testPart2Rando(self):
        self.assertEqual(reportRepairPart2([21,979,366,400,75,1456,1557,2000,1,92,63,2200,400,231]), 39236400)

