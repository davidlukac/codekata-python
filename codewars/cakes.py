# Cakes
# https://www.codewars.com/kata/525c65e51bf619685c000059

import math
import unittest
from typing import Dict


def cakes_1(recipe, available):
    # type: (Dict[str, int], Dict[str, int]) -> int
    lowest_available = math.inf

    for i, a in recipe.items():
        if i in available.keys():
            av = available.get(i) / a
            if lowest_available > av:
                lowest_available = av
        else:
            lowest_available = 0
            break

    return int(lowest_available)


def cakes(recipe, available):
    # type: (Dict[str, int], Dict[str, int]) -> int
    return min(available.get(i, 0) // recipe[i] for i in recipe)


class TestCakes(unittest.TestCase):
    def test(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEquals(cakes(recipe, available), 2, 'Wrong result for example #1')

        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        self.assertEquals(cakes(recipe, available), 0, 'Wrong result for example #2')
