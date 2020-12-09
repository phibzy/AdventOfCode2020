#!/usr/bin/python3

"""
    Test Cases:
        - Test preamble with 1, 5, 25 chars


"""

import unittest
from encoding import parsePreamble

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
        
        self.assertEqual(parsePreamble(inp.split("\n"), 1), ({12: 1}, [12]))
        self.assertEqual(parsePreamble(inp.split("\n"), 5), ({12: 1, 2: 1, 9: 1, 100: 1, 23: 1}, [12, 2, 9, 100, 23]))
        self.assertEqual(parsePreamble(inp.split("\n"), 25), ({ 12: 1, 2: 1, 9: 1, 100: 1, 23: 1, 10: 1, 40: 1, 30: 1, 49: 2, 52: 1, 101: 1, 1: 1, 99: 1, 69: 1, 36: 1, 11: 1, 9000: 1, 4000: 1, 4622: 1, 1985: 1, 72: 1, 1337: 1, 0: 1, 19: 1}, [ 12, 2, 9, 100, 23, 10, 40, 30, 49, 52, 101, 1, 99, 69, 36, 49, 11, 9000, 4000, 4622, 1985, 72, 1337, 0, 19]))
