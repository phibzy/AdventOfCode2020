#!/usr/bin/python4

"""
    Test Cases:
        - Parsing input
        - Cycle testing
        - Correct answer for test input

"""

import unittest
from cubes import parseSlice, cycle, updateCube, runCycles
from pathlib import Path

class testCube(unittest.TestCase):

    testPath = Path("./input/")
    testInput = [ parseSlice(f.read_text()) for f in sorted(testPath.glob("test*")) ]

    def testParse(self):
        self.assertEqual(self.testInput[0], [[
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.']
                                       ],
                                       [
                                        ['.','.','.','.','.'],
                                        ['.','.','#','.','.'],
                                        ['.','.','.','#','.'],
                                        ['.','#','#','#','.'],
                                        ['.','.','.','.','.']
                                       ],
                                       [
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.']
                                       ]]
                                        )

    def testCycle(self):
        self.assertEqual(cycle(self.testInput[0]), ([
                                      [
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.']
                                      ],
                                      [
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','#','.','.','.'],
                                        ['.','.','.','#','.'],
                                        ['.','.','#','.','.'],
                                        ['.','.','.','.','.']
                                       ],
                                       [
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','#','.','#','.'],
                                        ['.','.','#','#','.'],
                                        ['.','.','#','.','.'],
                                        ['.','.','.','.','.']
                                       ],
                                       [
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','#','.','.','.'],
                                        ['.','.','.','#','.'],
                                        ['.','.','#','.','.'],
                                        ['.','.','.','.','.']
                                       ],
                                       [
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.'],
                                        ['.','.','.','.','.']
                                       ]
                                    ], 11))

    def testUpdateCube(self):
        self.assertEqual(updateCube(self.testInput[0], 1, 2, 1, 3, 5, 5), "#")
        self.assertEqual(updateCube(self.testInput[0], 0, 2, 1, 3, 5, 5), "#")
        self.assertEqual(updateCube(self.testInput[0], 2, 2, 1, 3, 5, 5), "#")
        self.assertEqual(updateCube(self.testInput[0], 0, 3, 3, 3, 5, 5), "#")
        self.assertEqual(updateCube(self.testInput[0], 2, 3, 3, 3, 5, 5), "#")
        self.assertEqual(updateCube(self.testInput[0], 0, 4, 2, 3, 5, 5), "#")
        self.assertEqual(updateCube(self.testInput[0], 2, 4, 2, 3, 5, 5), "#")

        # Testing faulty cases
        self.assertEqual(updateCube(self.testInput[0], 0, 3, 0, 3, 5, 5), ".")
        self.assertEqual(updateCube(self.testInput[0], 1, 0, 2, 3, 5, 5), ".")

    def testRunCycles(self):
        self.assertEqual(runCycles(self.testInput[0], 1), 11)
        self.assertEqual(runCycles(self.testInput[0], 2), 21)
        self.assertEqual(runCycles(self.testInput[0], 3), 38)
