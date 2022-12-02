from aoc2022.day2 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day2", type="split")


def test_solve_part1():
    expected = 15
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 12
    actual = solution.solve_part2(input_data)
    assert expected == actual
