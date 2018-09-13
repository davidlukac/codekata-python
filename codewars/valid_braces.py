# Valid Braces
# http://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python


import unittest


def valid_braces(string: str) -> bool:
    stack = []

    braces = {')': '(', '}': '{', ']': '['}

    for l in string:
        if l in braces.values():
            stack.append(l)
        elif stack:
            if stack.pop() != braces[l]:
                # We are closing a brace which we didn't open last.
                return False
        else:
            # The stack was empty and we tried to remove a brace which is not valid.
            return False

    if stack:
        # List is not empty.
        return False
    else:
        return True


class ValidBracesTest(unittest.TestCase):
    def test(self):
        self.assertEqual(True, valid_braces("()"))
        self.assertEqual(valid_braces("[(])"), False)


if __name__ == '__main__':
    unittest.main()
