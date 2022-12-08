from aoc2022.day04 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day04", "csv")


def test_solve_part1():
    expected = 2
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 4
    actual = solution.solve_part2(input_data)
    assert expected == actual
