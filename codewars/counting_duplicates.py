# Counting Duplicates
# https://www.codewars.com/kata/counting-duplicates

import unittest
from collections import Counter


def duplicate_count(text: str) -> int:
    return len({l for l, count in Counter(text.lower()).items() if count > 1})


if __name__ == '__main__':
    unittest.main()


class CountingDuplicatesTest(unittest.TestCase):
    def test(self):
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("aabbcde"), 2)
        self.assertEqual(duplicate_count("aabbcdeB"), 2)
        self.assertEqual(duplicate_count("indivisibility"), 1)
        self.assertEqual(duplicate_count("IndivisibilIities"), 2)
        self.assertEqual(duplicate_count(" "), 0)
        self.assertEqual(duplicate_count("asdfghjkl;'\\"), 0)
        self.assertEqual(duplicate_count("asdfghjkl;'\\'"), 1)
        self.assertEqual(duplicate_count("aa11"), 2)
