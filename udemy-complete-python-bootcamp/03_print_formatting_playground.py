from typing import List, Dict, Tuple

"""
In this exercise we print float numbers with various lengths all aligned to the dot.
"""


def get_input_numbers() -> List[float]:
    a = 1.1
    b = 22.22
    c = 333.333
    d = 4444.4444
    e = 1.1234567789
    f = 1834781923491
    g = .1231
    h = 132841802340134.1

    return [a, b, c, d, e, f, g, h]


def calculate(numbers: List[float]) -> Tuple[Dict[float, Tuple[int, int, int, int, int]], int, int]:
    longest_l = 0
    longest_r = 0
    decimals = {}

    for n in numbers:
        f_num = float(n)
        str_num = str(f_num)

        l_part, r_part = tuple(str_num.split('.'))
        l_part_len = len(l_part)
        r_part_len = len(r_part)
        decimals[n] = (f_num, l_part, r_part, l_part_len, r_part_len)

        if l_part_len > longest_l:
            longest_l = l_part_len
        if r_part_len > longest_r:
            longest_r = r_part_len

    return decimals, longest_l, longest_r


def print_ver_1(
        original: List[float],
        calculated: Dict[float, Tuple[int, int, int, int, int]],
        longest_l: int, longest_r: int) -> None:
    print('Longest: {l}.{r}'.format(l=longest_l, r=longest_r))
    for n in original:
        actual_f = calculated[n][0]
        l_part = calculated[n][1]
        l_part_len = calculated[n][3]
        r_part = calculated[n][2]
        r_part_len = calculated[n][4]

        width = longest_l + 1 + r_part_len

        print('ver-1 N: {num:{fill}{width}}\t\t\t\tl: {l_part}[{l_part_len}] r: {r_part}[{r_part_len}]'
              .format(num=actual_f, fill='', width=width,
                      l_part=l_part, l_part_len=l_part_len, r_part=r_part, r_part_len=r_part_len))


def print_ver_2(
        original: List[float],
        calculated: Dict[float, Tuple[int, int, int, int, int]],
        longest_l: int, longest_r: int) -> None:
    print('Longest: {l}.{r}'.format(l=longest_l, r=longest_r))
    for n in original:
        l_part = calculated[n][1]
        l_part_len = calculated[n][3]
        r_part = calculated[n][2]
        r_part_len = calculated[n][4]

        print('ver-2 N: ' +
              '{l_num:{fill}>{l_width}}.{r_num:{fill}<{r_width}} l: {l_part}[{l_part_len}] r: {r_part}[{r_part_len}]'
              .format(l_num=l_part, l_width=longest_l, fill='', r_num=r_part, r_width=longest_r, l_part=l_part,
                      l_part_len=l_part_len, r_part=r_part, r_part_len=r_part_len))


if __name__ == '__main__':
    input_numbers = get_input_numbers()
    calc, lon_l, lon_r = calculate(input_numbers)
    print_ver_1(input_numbers, calc, lon_l, lon_r)
    print()
    print('---===---')
    print()
    print_ver_2(input_numbers, calc, lon_l, lon_r)
