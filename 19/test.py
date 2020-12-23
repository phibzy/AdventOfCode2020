#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from messages import parseInput, checkMessages, checkValid
from pathlib import Path
from pprint import pprint

class test(unittest.TestCase):

    testInput = [ parseInput(f.read_text()) for f in sorted(Path("./input/").glob("test*")) ]
    # pprint(testInput)

    def testMessages(self):
        self.assertEqual(checkMessages(*self.testInput[0]), 2)
        self.assertEqual(checkMessages(*self.testInput[2]), 3)
        self.assertEqual(checkMessages(*self.testInput[3]), 12)

    def testValid(self):
        # # Test input 1
        self.assertFalse(checkValid("a", self.testInput[0][0], "0", 0) )
        # # This will always fail since we handle that case
        # # in checkMessages function
        # # self.assertFalse(checkValid("abaaaaaaa", self.testInput[0][0], "0", 0) )

        self.assertTrue(checkValid("aba", self.testInput[0][0], "0", 0) )
        self.assertTrue(checkValid("aab", self.testInput[0][0], "0", 0) )

        # # # Test input 2
        self.assertFalse(checkValid("bababa", self.testInput[1][0], "0", 0) )
        self.assertFalse(checkValid("aaabbb", self.testInput[1][0], "0", 0) )

        self.assertTrue(checkValid("ababbb", self.testInput[1][0], "0", 0) )
        self.assertTrue(checkValid("abbbab", self.testInput[1][0], "0", 0) )

        # Testing for loop cases
        self.assertTrue(checkValid("babbbbaabbbbbabbbbbbaabaaabaaa", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("aaaaabbaabaaaaababaa", self.testInput[3][0], "0", 0) )

        self.assertTrue(checkValid("bbabbbbaabaabba", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("babbbbaabbbbbabbbbbbaabaaabaaa", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("aaabbbbbbaaaabaababaabababbabaaabbababababaaa", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("bbbbbbbaaaabbbbaaabbabaaa", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("bbbababbbbaaaaaaaabbababaaababaabab", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("ababaaaaaabaaab", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("ababaaaaabbbaba", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("baabbaaaabbaaaababbaababb", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("abbbbabbbbaaaababbbbbbaaaababb", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("aaaaabbaabaaaaababaa", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("aaaabbaabbaaaaaaabbbabbbaaabbaabaaa", self.testInput[3][0], "0", 0) )
        self.assertTrue(checkValid("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba", self.testInput[3][0], "0", 0) )

        self.assertTrue(checkValid("bbabbbbaabaabba", self.testInput[2][0], "0", 0) )
        self.assertTrue(checkValid("bbabbbbaabaabba", self.testInput[3][0], "0", 0) )

