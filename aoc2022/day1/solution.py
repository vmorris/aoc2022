from aoc2022.util import get_input


def _process_entries(entries):
    elves = []
    elf = []
    for i in entries:
        if i == "":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(i))
    return elves


def solve_part1(entries):
    elves = _process_entries(entries)
    max_calories = 0
    for elf in elves:
        calories = sum(elf)
        if calories > max_calories:
            max_calories = calories
    return max_calories


def solve_part2(entries):
    elves = _process_entries(entries)
    sums = []
    for elf in elves:
        sums.append(sum(elf))
    return sum(sorted(sums)[::-1][:3])


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day1/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
