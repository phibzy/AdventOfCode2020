#!/usr/bin/python4

"""
    Test Cases:
        - Default cases
        - 0 result



"""

import unittest
from adapter import findJoltDist, findPossiblePaths

# Auto read input from test* files?

class testAdapter(unittest.TestCase):

    def testFindJoltDistAndPt2(self):
        t1 = r"""16
10
15
5
1
11
7
19
6
12
4"""

        self.assertEqual(findJoltDist(convertInput(t1))[0], 35)
        # self.assertEqual(findPossiblePaths(convertInput(t1)), 8)

        t2 = r"""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

        self.assertEqual(findJoltDist(convertInput(t2))[0], 220)
        # self.assertEqual(findPossiblePaths(convertInput(t2)), 19208)


    def testPaths(self):
        # Only one possible path
        t1 = [3,6,9,12]
        self.assertEqual(findPossiblePaths(t1), 1)
        self.assertEqual(findPossiblePaths([0,1,4,5,6,7,10]), 4)

def convertInput(inp):
    return list(map(int, inp.split("\n")))

