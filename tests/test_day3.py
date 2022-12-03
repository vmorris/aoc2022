from aoc2022.day3 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day3")


def test_solve_part1():
    expected = 157
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 70
    actual = solution.solve_part2(input_data)
    assert expected == actual
