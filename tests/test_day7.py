from aoc2022.day7 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day7")


def test_solve_part1():
    expected = 95437
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 24933642
    actual = solution.solve_part2(input_data)
    assert expected == actual
