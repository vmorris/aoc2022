from aoc2022.util import get_input

from typing import List


class CPU:
    def __init__(self, storage: List, debug_cycles: List = None):
        self.cycle = 1
        self.X = 1
        self.IP = 0
        self.storage = storage
        self.debug_cycles = debug_cycles
        self.signal_strengths = []

    def load_storage(self, data: List = None):
        self.storage = data

    def tick(self):
        if self.cycle in self.debug_cycles:
            self.signal_strengths.append(self.cycle * self.X)
        self.cycle += 1

    def run(self):
        try:
            while True:
                self.step()
        except IndexError:
            pass

    def step(self):
        instruction = self.fetch()
        self.decode_execute(instruction)
        self.IP += 1

    def fetch(self):
        return self.storage[self.IP]

    def decode_execute(self, instruction: str):
        instruction = instruction.split()
        if instruction[0] == "noop":
            self._noop()
        elif instruction[0] == "addx":
            self._addx(int(instruction[1]))

    def _noop(self):
        self.tick()

    def _addx(self, arg1: int):
        self.tick()
        self.tick()
        self.X += arg1


class CRT:
    def __init__(self):
        self.display = "." * 240

    def __repr__(self):
        chunks = []
        for row in range(6):
            chunks.append(self.display[row * 40 : (row * 40) + 40])
        return "\n".join(chunks)


def solve_part1(entries):
    debug_cycles = [20, 60, 100, 140, 180, 220]
    cpu = CPU(entries, debug_cycles)
    cpu.run()
    return sum(cpu.signal_strengths)


def solve_part2(entries):
    cpu = CPU(entries)
    crt = CRT()
    return crt.__repr__()


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day10/input")
    print(solve_part1(entries))
    # print(solve_part2(entries))
