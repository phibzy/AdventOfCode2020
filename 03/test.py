#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from slope import stepSearch, totalTrees

class testSlope(unittest.TestCase):

    def testSSPt1Default(self):
        grid = r"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        self.assertEqual(stepSearch(str2List(grid), 3, 1), 7)
        self.assertEqual(stepSearch(str2List(grid), 0, 1), 3)
        self.assertEqual(stepSearch(str2List(grid), 5, 5), 2)
        self.assertEqual(stepSearch(str2List(grid), 2, 2), 1)

    def testSSPt1Diff(self):
        grid = r"""#.##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.#####..
.#.#.#....#
.#.#.#..###
#.##...#..#
#...##.#..#
.#..#..##.#"""
        self.assertEqual(stepSearch(str2List(grid), 3, 1), 8)
        self.assertEqual(stepSearch(str2List(grid), 0, 1), 4)
        self.assertEqual(stepSearch(str2List(grid), 5, 5), 3)
        self.assertEqual(stepSearch(str2List(grid), 2, 2), 2)

    def testTotal(self):
        grid = r"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
        
        self.assertEqual(totalTrees(str2List(grid), [[3,1],[0,1],[5,5],[2,2]]), 42)
        self.assertEqual(totalTrees(str2List(grid), [[1,1],[3,1],[5,1],[7,1],[1,2]]), 336)


def str2List(s):
    s = s.split()
    res = list()

    for line in s:
        res.append(line.strip())

    return res

