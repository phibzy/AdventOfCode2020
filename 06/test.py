#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from customs import groupCount, totalCount

class test(unittest.TestCase):

    def testGroupCount1(self):
        self.assertEqual(groupCount(['a','b','c','d','e'], 1), 5)
        self.assertEqual(groupCount(['aed','adb','acc','ad','ae'], 1), 5)
        self.assertEqual(groupCount(['a','a','a','a','a'], 1), 1)
        self.assertEqual(groupCount(['aaZaaa'], 1), 1)

    def testGroupCount2(self):
        self.assertEqual(groupCount(['a','b','c','d','e'], 2), 0)
        self.assertEqual(groupCount(['aed','adb','acc','ad','ae'], 2), 1)
        self.assertEqual(groupCount(['a','a','a','a','a'], 2), 1)
        self.assertEqual(groupCount(['aaZaaa'], 2), 1)
        self.assertEqual(groupCount(['aed','adeb','acec','ead','ae'], 2), 2)
        self.assertEqual(groupCount(['aed','adb','acc','ad','ae'], 2), 1)
        self.assertEqual(groupCount(['aed','adb','acc','ad','ae'], 2), 1)
        self.assertEqual(groupCount(['abcdefg'], 2), 7)
        self.assertEqual(groupCount(['abcdefg', "zqp", "xyu"], 2), 0)

    def testTotalCount(self):
        s = r"""abc

a
b
c

ab
ac

a
a
a
a

b"""
        self.assertEqual(totalCount(s, 1), 11)
        self.assertEqual(totalCount(s, 2), 6)
