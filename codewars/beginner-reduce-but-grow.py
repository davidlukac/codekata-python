# Beginner - Reduce but Grow
# http://www.codewars.com/kata/beginner-reduce-but-grow/python

import unittest
from functools import reduce


def grow(arr: list):
    return reduce(lambda x, y: x * y, arr)


class GrowTest(unittest.TestCase):
    def test(self):
        self.assertEqual(6, grow([1, 2, 3]))
        self.assertEqual(16, grow([4, 1, 1, 1, 4]))
        self.assertEqual(64, grow([2, 2, 2, 2, 2, 2]))


if __name__ == '__main__':
    unittest.main()
