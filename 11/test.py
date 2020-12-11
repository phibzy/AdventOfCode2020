#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from seating import parseInput, updateGrid, countAround, updateSeat 
from pathlib import Path

class testSeating(unittest.TestCase):

    inputPath = Path('./input/')

    # So that we can 1-index based on filenames
    # FUN FACT: filesystem order is not necessarily alphabetical order
    testFileContents = [x.read_text() for x in sorted(inputPath.glob('test*')) if not x.is_dir()]
    testFileContents = [0] + testFileContents

    def testParseInput(self):

        grid1 = [['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
                 ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
                 ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'],
                 ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
                 ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
                 ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
                 ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'],
                 ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
                 ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'],
                 ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']]

        self.assertEqual(parseInput(self.testFileContents[1]), grid1)
        
    # def testUpdateGrid(self):
        # self.assertEqual(updateGrid(self.testFileContents[1]), self.testFileContents[2])
        # self.assertEqual(updateGrid(self.testFileContents[2]), self.testFileContents[3])
        # self.assertEqual(updateGrid(self.testFileContents[3]), self.testFileContents[4])
        # self.assertEqual(updateGrid(self.testFileContents[4]), self.testFileContents[5])
        # self.assertEqual(updateGrid(self.testFileContents[5]), self.testFileContents[6])

    def testCountAround(self):
        self.assertEqual(countAround(parseInput(self.testFileContents[1]), 0, 0), 0) 
        self.assertEqual(countAround(parseInput(self.testFileContents[1]), 0, 500), 0) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 0), 2) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 9), 3) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 0), 2) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 9), 3) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 8, 3), 8) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 9, 9), 2) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 9, 0), 1) 



