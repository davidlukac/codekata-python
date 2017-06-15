# Shortest word
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

import unittest


def find_short(s: str) -> int:
    return next(iter(sorted(list(map(lambda word: len(word), s.split())))))


def find_short_2(s: str) -> int:
    return min(len(w) for w in s.split())


if __name__ == '__main__':
    unittest.main()


class ShortestWord(unittest.TestCase):
    def impl_1_test(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
        self.assertEqual(find_short("lets talk about javascript the best language"), 3)
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1)
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)
        
    def impl_2_test(self):
        self.assertEqual(find_short_2("bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEqual(find_short_2("turns out random test cases are easier than writing out basic ones"), 3)
        self.assertEqual(find_short_2("lets talk about javascript the best language"), 3)
        self.assertEqual(find_short_2("i want to travel the world writing code one day"), 1)
        self.assertEqual(find_short_2("Lets all go on holiday somewhere very cold"), 2)
