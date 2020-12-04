#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from passport import pid, ecl, hcl, hgt, eyr, iyr, byr
from passport import checkFields, strToInput, checkPassport

class testPassport(unittest.TestCase):

    def testCheckPid(self):
        # valid tests
        self.assertTrue(pid("099999999"))
        self.assertTrue(pid("000000009"))
        self.assertTrue(pid("123456789"))

        # invalid tests
        self.assertFalse(pid("0999599999"))
        self.assertFalse(pid("99a599999"))
        self.assertFalse(pid("99\n599999"))
        self.assertFalse(pid("99a5999 9"))

    def testHcl(self):
        # valid tests
        self.assertTrue(hcl("#92f40e"))
        
        # invalid tests
        self.assertFalse(hcl("92f40e"))
        self.assertFalse(hcl("#0gf40e"))
        self.assertFalse(hcl("#040e"))
        self.assertFalse(hcl("#040e29g"))

    def testEcl(self):
        # valid tests
        self.assertTrue(ecl("amb"))
        self.assertTrue(ecl("blu"))
        self.assertTrue(ecl("brn"))
        self.assertTrue(ecl("gry"))
        self.assertTrue(ecl("grn"))
        self.assertTrue(ecl("hzl"))
        self.assertTrue(ecl("oth"))

        # invalid tests
        self.assertFalse(ecl("red"))



