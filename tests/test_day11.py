from aoc2022.day11 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day11", "nlnl")


def test_solve_part1():
    solution.make_monkeys(input_data)
    expected = 10605
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = 2713310158
    actual = solution.solve_part2(input_data)
    assert expected == actual
