#!/usr/bin/python3

"""
    Test Cases:



"""

import unittest
from messages import parseInput
from pathlib import Path
from pprint import pprint

class test(unittest.TestCase):

    testInput = [ parseInput(f.read_text()) for f in sorted(Path("./input/").glob("test*")) ]
    pprint(testInput)

    def test(self):
        pass

