#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from handheld import parseInput, findValue, fixedValue

class testHandheld(unittest.TestCase):

    def testParseInput(self):
        t2 = r"acc -3"
        self.assertEqual(parseInput(t2), [("acc", "-", "3")]) 
        # t1 = r"""nop +44
# acc -3
# jmp +7
# nop +0
# nop -10
# acc +2
# jmp -2"""

        # self.assertEqual(parseInput(t1), [("nop", "+", "44"), ("acc", "-", "3"), ("jmp", "+", "7"), ("nop", "+", "0"),
                                          # ("nop", "-", "10"), ("acc", "+", "2"), ("jmp", "-", "2")])

