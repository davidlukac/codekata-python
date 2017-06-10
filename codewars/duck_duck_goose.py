# Duck Duck Goose
# http://www.codewars.com/kata/duck-duck-goose

import unittest
from typing import List


class Player:
    def __init__(self, name: str):
        self.name = name


def duck_duck_goose(players: List[Player], goose: int) -> str:
    return players[goose % len(players) - 1].name


class TestDuckDuckGoose(unittest.TestCase):
    l = [Player('a'), Player('b'), Player('c')]

    def first_round_test(self):
        self.assertEqual(duck_duck_goose(self.l, 1), 'a')

    def second_round_test(self):
        self.assertEqual(duck_duck_goose(self.l, 4), 'a')

if __name__ == '__main__':
    unittest.main()
