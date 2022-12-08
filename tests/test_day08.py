from aoc2022.day08 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day08", type="int-matrix")


def test_solve_part1():
    expected = 21
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 8
    actual = solution.solve_part2(input_data)
    assert expected == actual
