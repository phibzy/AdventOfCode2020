#!/usr/bin/python3

"""
    Test Cases:
        - Test preamble with 1, 5, 25 chars


"""

import unittest
from encoding import parsePreamble, findNumber, checkSum
from collections import deque

class testEncoding(unittest.TestCase):

    def testParsePreamble(self):
        inp = r"""12
2
9
100
23
10
40
30
49
52
101
1
99
69
36
49
11
9000
4000
4622
1985
72
1337
0
19
2000"""
        
        self.assertEqual(parsePreamble(inp.split("\n"), 1), ({12: 1}, deque([12])))
        self.assertEqual(parsePreamble(inp.split("\n"), 5), ({12: 1, 2: 1, 9: 1, 100: 1, 23: 1}, deque([12, 2, 9, 100, 23])))
        self.assertEqual(parsePreamble(inp.split("\n"), 25), ({ 12: 1, 2: 1, 9: 1, 100: 1, 23: 1, 10: 1, 40: 1, 30: 1, 49: 2, 52: 1, 101: 1, 1: 1, 99: 1, 69: 1, 36: 1, 11: 1, 9000: 1, 4000: 1, 4622: 1, 1985: 1, 72: 1, 1337: 1, 0: 1, 19: 1}, deque([ 12, 2, 9, 100, 23, 10, 40, 30, 49, 52, 101, 1, 99, 69, 36, 49, 11, 9000, 4000, 4622, 1985, 72, 1337, 0, 19])))

    def testCheckSum(self):
        # valid cases
        self.assertTrue(checkSum(21, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))
        self.assertTrue(checkSum(14, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))
        self.assertTrue(checkSum(123, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))
        self.assertTrue(checkSum(21, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))

        # invalid cases
        self.assertFalse(checkSum(12, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))
        self.assertFalse(checkSum(23, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))
        self.assertFalse(checkSum(121, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))
        self.assertFalse(checkSum(1021, {12: 1, 2: 1, 9: 1, 100: 1, 23: 1}))

    def testFindNumber(self):
        inp = r"""12
2
9
100
23
11
40
30
49
52
101
1
99
69
36
49
11
9000
4000
4622
1985
72
1337
0
19
2
60
2000"""

        self.assertEqual(findNumber(inp.split("\n"), 5, *parsePreamble(inp.split("\n"), 5)), 40)
        self.assertEqual(findNumber(inp.split("\n"), 25, *parsePreamble(inp.split("\n"), 25)), 2000)

        # test for char no longer in sequence
        # self.assertEqual(findNumber(inp.split("\n"), 5, *parsePreamble(inp.split("\n"), 5)), 2000)
