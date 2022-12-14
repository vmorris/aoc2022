from aoc2022.day10 import solution
from aoc2022.util import get_input


input_data = get_input("tests/testinput.day10")


def test_solve_part1():
    expected = 13140
    actual = solution.solve_part1(input_data)
    assert expected == actual


def test_solve_part2():
    expected = [
        "##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######.....",
        "",
    ]
    actual = solution.solve_part2(input_data)
    assert "\n".join(expected) == actual
