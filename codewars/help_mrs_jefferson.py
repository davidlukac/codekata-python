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

    def get_low_start(any_dist: int, any_n: int) -> (int, bool):
        r = any_n / any_dist - any_dist / 2 + 1 / 2
        return int(r), r.is_integer()

    highest_distance = int(floor(2 * sqrt(n)))
    distances = (distance for distance in range(2, highest_distance - 1)
                 if ((distance % 2) == 0 and n % (distance / 2) == 0)
                 or ((distance % 2) > 0 and (n % distance) == 0))

    for distance in distances:
        low_start, start_is_int = get_low_start(distance, n)
        if start_is_int:
            return list(reversed(range(low_start, low_start + distance)))

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
