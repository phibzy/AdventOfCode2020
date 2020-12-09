#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from handheld import parseInput, findValue, fixedValue

class testHandheld(unittest.TestCase):

    def testParseInput(self):
        t1 = r"""nop +44
acc -3
jmp +7
nop +0
nop -10
acc +2
jmp -2"""

        self.assertEqual(parseInput(t1), [("nop", "+", "44"), ("acc", "-", "3"), ("jmp", "+", "7"), ("nop", "+", "0"),
                                          ("nop", "-", "10"), ("acc", "+", "2"), ("jmp", "-", "2")])

    def testFindValue(self):
        t1 = r"""nop +44
acc -3
jmp +3
nop +0
nop -10
acc +2
jmp -2"""

        self.assertEqual(findValue(parseInput(t1), dict(), 0)[0], -1)
        self.assertEqual(findValue(parseInput(t1), dict(), 0)[1], True)


        self.assertEqual(len(findValue(parseInput(t1), dict(), 0)[2]), 2)
        self.assertEqual(len(findValue(parseInput(t1), dict(), 0)[3]), 2)

        t2 = r"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

        self.assertEqual(findValue(parseInput(t2), dict(), 0)[0], 5)
        self.assertEqual(findValue(parseInput(t2), dict(), 0)[1], True)
        self.assertEqual(len(findValue(parseInput(t2), dict(), 0)[2]), 3)
        self.assertEqual(len(findValue(parseInput(t2), dict(), 0)[3]), 1)

        t3 = r"""nop +0
acc +1
acc +3
acc +1
acc +6"""

        self.assertEqual(findValue(parseInput(t3), dict(), 0)[0], 11)
        self.assertEqual(findValue(parseInput(t3), dict(), 0)[1], False)
        self.assertEqual(len(findValue(parseInput(t3), dict(), 0)[2]), 0)
        self.assertEqual(len(findValue(parseInput(t3), dict(), 0)[3]), 1)

    def testFixedValue(self):
        t1 = r"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
        self.assertEqual(fixedValue(parseInput(t1)), 8)
