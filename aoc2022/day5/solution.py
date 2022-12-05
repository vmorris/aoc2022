from aoc2022.util import get_input

from collections import defaultdict
from string import ascii_uppercase


def process_input(entries):
    split = entries.index("")
    stacks = entries[:split]
    instructions = entries[split + 1 :]
    stacks.pop()
    stacks.reverse()
    _stacks = defaultdict(list)
    for data in stacks:
        # clean up data
        data = data[1::4]
        # build our stacks
        for i, d in enumerate(data):
            if d in ascii_uppercase:
                _stacks[i + 1].append(d)
    return (_stacks, instructions)


def parse_instruction(inst):
    parts = inst.split()
    num = int(parts[1])
    start = int(parts[3])
    end = int(parts[5])
    return (num, start, end)


def solve_part1(entries):
    stacks, instructions = process_input(entries)
    for i in instructions:
        num_to_move, origin, destination = parse_instruction(i)
        for _ in range(num_to_move):
            crate = stacks[origin].pop()
            stacks[destination].append(crate)
    result = ""
    for stack in stacks.values():
        result += stack.pop()
    return result


def solve_part2(entries):
    stacks, instructions = process_input(entries)
    for i in instructions:
        num_to_move, origin, destination = parse_instruction(i)
        hold = []
        for _ in range(num_to_move):
            hold.append(stacks[origin].pop())
        hold.reverse()
        for crate in hold:
            stacks[destination].append(crate)
    result = ""
    for stack in stacks.values():
        result += stack.pop()
    return result


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day5/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
