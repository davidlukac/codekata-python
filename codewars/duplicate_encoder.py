# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

import unittest
from collections import Counter


def duplicate_encode(word: str) -> str:
    word = word.lower()
    counts = Counter(word)
    return ''.join(['(' if counts[l] == 1 else ')' for l in word])


if __name__ == '__main__':
    unittest.main()


class DuplicateEncoderTest(unittest.TestCase):
    def test(self):
        self.assertEquals(duplicate_encode("din"), "(((")
        self.assertEquals(duplicate_encode("recede"), "()()()")
        self.assertEquals(duplicate_encode("Success"), ")())())", "should ignore case")
        self.assertEquals(duplicate_encode("(( @"), "))((")
