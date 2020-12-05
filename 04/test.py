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

    def testHgt(self):
        # valid tests
        self.assertTrue(hgt("193cm"))
        self.assertTrue(hgt("165cm"))
        self.assertTrue(hgt("150cm"))
        self.assertTrue(hgt("59in"))
        self.assertTrue(hgt("76in"))

        # invalid tests
        self.assertFalse(hgt("193in"))
        self.assertFalse(hgt("165in"))
        self.assertFalse(hgt("149cm"))
        self.assertFalse(hgt("59cm"))
        self.assertFalse(hgt("76cm"))
        self.assertFalse(hgt("58cm"))
        self.assertFalse(hgt("1cm"))
        self.assertFalse(hgt("77cm"))
        self.assertFalse(hgt("1000004cm"))

    def testByr(self):
        # valid
        self.assertTrue(byr("1920"))
        self.assertTrue(byr("2002"))
        self.assertTrue(byr("1957"))

        # invalid
        self.assertFalse(byr("1919"))
        self.assertFalse(byr("20020000"))
        self.assertFalse(byr("2003"))
        self.assertFalse(byr("001940"))

    def testIyr(self):
        # valid
        self.assertTrue(iyr("2010"))
        self.assertTrue(iyr("2020"))
        self.assertTrue(iyr("2012"))

        # invalid
        self.assertFalse(iyr("002010"))
        self.assertFalse(iyr("20020000"))
        self.assertFalse(iyr("2009"))
        self.assertFalse(iyr("2021"))

    def testEyr(self):
        # valid
        self.assertTrue(eyr("2030"))
        self.assertTrue(eyr("2020"))
        self.assertTrue(eyr("2022"))

        # invaled
        self.assertFalse(eyr("002020"))
        self.assertFalse(eyr("20020000"))
        self.assertFalse(eyr("2019"))
        self.assertFalse(eyr("2031"))

    def testCheckFields(self):
        # valid
        self.assertTrue(checkFields("eyr","2030"))
        self.assertTrue(checkFields("iyr","2020"))
        self.assertTrue(checkFields("byr","1930"))
        self.assertTrue(checkFields("hgt","150cm"))
        self.assertTrue(checkFields("hgt","59in"))
        self.assertTrue(checkFields("hcl","#2293aa"))
        self.assertTrue(checkFields("ecl","amb"))
        self.assertTrue(checkFields("pid","000003957"))

        # invaled
        self.assertFalse(checkFields("eyr","2031"))
        self.assertFalse(checkFields("iyr","20020"))
        self.assertFalse(checkFields("byr","1903"))
        self.assertFalse(checkFields("hgt","149cm"))
        self.assertFalse(checkFields("hgt","58in"))
        self.assertFalse(checkFields("hcl","#22793aa"))
        self.assertFalse(checkFields("ecl","amnb"))
        self.assertFalse(checkFields("pid","00880003957"))

