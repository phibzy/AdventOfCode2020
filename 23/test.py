#!/usr/bin/python3

"""
    Test Cases:
        - Picking up cups that wrap around
        - 


"""

import unittest
from pathlib import Path
from crabCups import parseInput, playGame, moveCups

class testCrabs(unittest.TestCase):

    testInput = [ parseInput(f.read_text()) for f in sorted(Path("./input/").glob("test*")) ]

    def testParse(self):
        self.assertEqual(self.testInput[0], [3,8,9,1,2,5,4,6,7])

    def testMoveCups(self):
        self.assertEqual(moveCups(self.testInput[0], 0), [3,2,8,9,1,5,4,6,7]) 

        # # edge cases
        # self.assertEqual(moveCups(self.testInput[0], 8), [1,2,5,4,6,3,8,9,7]) 
        # self.assertEqual(moveCups(self.testInput[0], 7), [9,1,2,5,7,3,8,4,6]) 
        # self.assertEqual(moveCups(self.testInput[0], 6), [8,9,1,2,6,7,3,5,4]) 
        # self.assertEqual(moveCups(self.testInput[0], 5), [3,4,6,7,8,9,1,2,5]) 

    def testPlayGame(self):
        # self.assertEqual(playGame(self.testInput[0], 1), [3,2,8,9,1,5,4,6,7])
        # self.assertEqual(playGame(self.testInput[0], 2), [3,2,5,4,6,7,8,9,1])
        # self.assertEqual(playGame(self.testInput[0], 3), [7,2,5,8,9,1,3,4,6])
        # self.assertEqual(playGame(self.testInput[0], 5), [9,2,5,8,4,1,3,6,7])
        self.assertEqual(playGame(self.testInput[0], 10), [9,2,6,5,8,3,7,4])
        self.assertEqual(playGame(self.testInput[0], 100), [6,7,3,8,4,5,2,9])
