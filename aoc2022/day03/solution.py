from aoc2022.util import get_input, divide_chunks

import string


def get_letter_value(letter):
    return string.ascii_letters.index(letter) + 1


def solve_part1(entries):
    items = []
    for rucksack in entries:
        half = int(len(rucksack) / 2)
        compartment_1 = set(rucksack[:half])
        compartment_2 = set(rucksack[half:])
        mistaken_item = compartment_1.intersection(compartment_2)
        items.append(mistaken_item.pop())
    return sum(map(get_letter_value, items))


def solve_part2(entries):
    items = []
    elf_triplets = divide_chunks(entries, 3)
    for group in elf_triplets:
        sack1 = set(group[0])
        sack2 = set(group[1])
        sack3 = set(group[2])
        badge_item = sack1.intersection(sack2).intersection(sack3)
        items.append(badge_item.pop())
    return sum(map(get_letter_value, items))


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day03/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
