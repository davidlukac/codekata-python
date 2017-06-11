# Help Mrs Jefferson
# http://www.codewars.com/kata/help-mrs-jefferson

import unittest
from math import floor, sqrt
from typing import List


def shortest_arrang(n: int) -> List[int]:
    """ https://cs.stackexchange.com/questions/24552/divide-an-integer-into-the-sum-of-consecutive-positive-numbers
    :param n: int
        Number to divide.
    :return: list
        List of group sizes, -1 if no solution.
    """
    def get_low_start(any_k: int) -> float:
        fn = float(n)
        fk = float(any_k)
        return fn / fk - fk / 2 + 1 / 2

    highest_k = int(floor(2 * sqrt(n)))
    ks = (k for k in range(2, highest_k - 1)
          if ((k % 2) == 0 and n % (k / 2) == 0)
          or ((k % 2) > 0 and (n % k) == 0))

    for k in ks:
        a = get_low_start(k)
        if a.is_integer():
            ia = int(a)
            res = list(reversed(range(ia, ia + k)))
            return res

    return [-1]


if __name__ == '__main__':
    unittest.main()


class MrsJeffersonTest(unittest.TestCase):
    def test(self):
        self.assertEqual(shortest_arrang(15), [8, 7])
        self.assertEqual(shortest_arrang(10), [4, 3, 2, 1])
        self.assertEqual(shortest_arrang(14), [5, 4, 3, 2])
        self.assertEqual(shortest_arrang(16), [-1])
        self.assertEqual(shortest_arrang(22), [7, 6, 5, 4])
        self.assertEqual(shortest_arrang(65), [33, 32])
