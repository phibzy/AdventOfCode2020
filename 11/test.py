#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from seating import parseInput, updateGrid, countAround, updateSeat, sumSeats
from pathlib import Path
import pprint

class testSeating(unittest.TestCase):

    inputPath = Path('./input/')

    # So that we can 1-index based on filenames
    # FUN FACT: filesystem order is not necessarily alphabetical order
    testFileContents = [x.read_text() for x in sorted(inputPath.glob('test*')) if not x.is_dir()]
    testFileContents = [0] + testFileContents

    parsedContents = list(map(parseInput, testFileContents[1:]))
    parsedContents = [0] + parsedContents

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
        # self.assertEqual(parseInput(self.testFileContents[1]), self.parsedContents[1])
        
    def testUpdateGrid(self):
        self.assertEqual(updateGrid(self.parsedContents[1]), self.parsedContents[2])
        self.assertEqual(updateGrid(self.parsedContents[2]), self.parsedContents[3])
        self.assertEqual(updateGrid(self.parsedContents[3]), self.parsedContents[4])
        self.assertEqual(updateGrid(self.parsedContents[4]), self.parsedContents[5])
        self.assertEqual(updateGrid(self.parsedContents[5]), self.parsedContents[6])

    def testCountAround(self):
        self.assertEqual(countAround(parseInput(self.testFileContents[1]), 0, 0), 0) 
        self.assertEqual(countAround(self.parsedContents[1], 0, 0), 0)

        self.assertEqual(countAround(parseInput(self.testFileContents[1]), 0, 500), 0) 
        self.assertEqual(countAround(self.parsedContents[1], 0, 500), 0)

        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 0), 2) 
        self.assertEqual(countAround(self.parsedContents[2], 0, 0), 2)

        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 9), 3) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 0), 2) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 0, 9), 3) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 8, 3), 8) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 9, 9), 2) 
        self.assertEqual(countAround(parseInput(self.testFileContents[2]), 9, 9), 2) 

        self.assertEqual(countAround(self.parsedContents[3], 0, 5), 1)

    def testUpdateSeat(self):
        self.assertEqual(updateSeat(self.parsedContents[3], 0, 5), "L")
        self.assertEqual(updateSeat(self.parsedContents[3], 3, 5), "#")

    def testSumSeats(self):
        self.assertEqual(sumSeats(self.parsedContents[6]), 37)
