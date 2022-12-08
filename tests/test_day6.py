from aoc2022.day6 import solution


input_data = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


def test_solve_part1():
    expected = [
        7,
        5,
        6,
        10,
        11,
    ]
    for index, data in enumerate(input_data):
        actual = solution.solve_part1(data)
        assert expected[index] == actual


def test_solve_part2():
    expected = [
        19,
        23,
        23,
        29,
        26,
    ]
    for index, data in enumerate(input_data):
        actual = solution.solve_part2(data)
        assert expected[index] == actual
