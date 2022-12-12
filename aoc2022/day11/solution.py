from aoc2022.util import get_input

from math import floor
from dataclasses import dataclass
from typing import Callable


def make_op_fun(input):
    arg1, op, arg2 = input.split()

    def mul1(arg):
        return arg * int(arg2)

    def mul2(arg):
        return arg * arg

    def add1(arg):
        return arg + int(arg2)

    def add2(arg):
        return arg + arg

    if arg2 != "old":
        if op == "*":
            return mul1
        elif op == "+":
            return add1
    elif arg1 == "old" and arg2 == "old":
        if op == "*":
            return mul2
        elif op == "+":
            return add2


def make_monkeys(entries):
    monkeys = []
    for monkey_in in entries:
        id = int(monkey_in[0].split()[1][:-1])
        items = list(map(int, monkey_in[1].split(":")[1].split(",")))
        operation = monkey_in[2].split(":")[1].split("=")[1]
        op_fun = make_op_fun(operation)
        test_divisible = int(monkey_in[3].split()[3])
        true_monkey_id = int(monkey_in[4].split()[-1])
        false_monkey_id = int(monkey_in[5].split()[-1])
        monkey_out = Monkey(
            id=id,
            items=items,
            op_fun=op_fun,
            test_divisible=test_divisible,
            true_monkey_id=true_monkey_id,
            false_monkey_id=false_monkey_id,
        )
        monkeys.append(monkey_out)
    return monkeys


def get_monkey_by_id(id, monkeys):
    for monkey in monkeys:
        if monkey.id == id:
            return monkey


@dataclass
class Monkey:
    id: int
    items: list
    op_fun: Callable[[int], int]
    test_divisible: int
    true_monkey_id: int
    false_monkey_id: int
    inspection_count: int = 0

    def operation(self, old):
        return self.op_fun(old)

    def take_turn(self, monkeys, low_stress=True, common_divisor=1):
        for item in self.items:
            item = self.operation(item)
            if low_stress:
                item = floor(item / 3)
            else:
                item = item % common_divisor
            if item % self.test_divisible == 0:
                target = get_monkey_by_id(self.true_monkey_id, monkeys)
            else:
                target = get_monkey_by_id(self.false_monkey_id, monkeys)
            target.items.append(item)
            self.inspection_count += 1
        self.items = []


def monkey_madness(monkeys, turns, low_stress, common_divisor):
    for _ in range(turns):
        for monkey in monkeys:
            monkey.take_turn(monkeys, low_stress, common_divisor)
    counts = sorted(list(monkey.inspection_count for monkey in monkeys))
    return counts[-1] * counts[-2]


def solve_part1(entries):
    monkeys = make_monkeys(entries)
    return monkey_madness(
        monkeys,
        turns=20,
        low_stress=True,
        common_divisor=1,
    )


def solve_part2(entries):
    monkeys = make_monkeys(entries)
    common_divisor = 1
    for monkey in monkeys:
        common_divisor *= monkey.test_divisible
    return monkey_madness(
        monkeys,
        turns=10000,
        low_stress=False,
        common_divisor=common_divisor,
    )


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day11/input", "nlnl")
    print(solve_part1(entries))
    print(solve_part2(entries))
