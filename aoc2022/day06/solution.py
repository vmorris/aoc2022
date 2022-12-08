from aoc2022.util import get_input


def count_unique(datastream):
    return len(set(datastream))


def locate_marker(datastream, length):
    for index in range(len(datastream)):
        chunk = datastream[index : index + length]
        if count_unique(chunk) == length:
            return index + length


def solve_part1(datastream):
    length = 4
    return locate_marker(datastream, length)


def solve_part2(datastream):
    length = 14
    return locate_marker(datastream, length)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day06/input", "single_str")
    print(solve_part1(entries))
    print(solve_part2(entries))
