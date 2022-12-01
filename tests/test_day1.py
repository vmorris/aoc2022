from aoc2022.day1 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day1", "int")


def test_solve_part1():
    expected = None
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = None
    actual = solution.solve_part2(input_data)
    assert expected == actual
