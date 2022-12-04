from aoc2022.util import get_input


def area_id_set(sections):
    start, end = map(int, sections.split("-"))
    return set(range(start, end + 1))


def solve_part1(entries):
    """In how many assignment pairs does one range fully contain the other?"""
    result = 0
    for elf1, elf2 in entries:
        area1 = area_id_set(elf1)
        area2 = area_id_set(elf2)
        if area1.issubset(area2) or area2.issubset(area1):
            result += 1
    return result


def solve_part2(entries):
    """In how many assignment pairs do the ranges overlap?"""
    result = 0
    for elf1, elf2 in entries:
        area1 = area_id_set(elf1)
        area2 = area_id_set(elf2)
        if len(area1.intersection(area2)) != 0:
            result += 1
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day4/input", "csv")
    print(solve_part1(entries))
    print(solve_part2(entries))
