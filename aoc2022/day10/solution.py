from aoc2022.util import get_input

from typing import List


class CRT:
    WIDTH = 40
    HEIGHT = 6
    PIXELS = WIDTH * HEIGHT

    def __init__(self):
        self.display = [False] * CRT.PIXELS

    def set_pixel(self, cycle, offset):
        pixel = cycle - 1
        col = pixel % CRT.WIDTH
        self.display[pixel] = abs(col - offset) <= 1

    def __repr__(self):
        output = ""
        for row in range(CRT.HEIGHT):
            for col in range(CRT.WIDTH):
                index = row * CRT.WIDTH + col
                output += "#" if self.display[index] else "."
            output += "\n"
        return output


class CPU:
    def __init__(self, storage: List, debug_cycles: List = None, crt: CRT = None):
        self.cycle = 1
        self.X = 1
        self.IP = 0
        self.storage = storage
        self.debug_cycles = debug_cycles
        self.signal_strengths = []
        self.step_count = 0
        self.crt = crt

    def load_storage(self, data: List = None):
        self.storage = data

    def store_signal(self):
        if self.debug_cycles and self.cycle in self.debug_cycles:
            self.signal_strengths.append(self.cycle * self.X)

    def run(self):
        try:
            while True:
                self.step()
        except IndexError:
            pass

    def step(self):
        if self.crt:
            self.crt.set_pixel(self.cycle, self.X)
        instruction = self.fetch(self.IP)
        self.decode_execute(instruction)
        self.cycle += 1

    def fetch(self, ip):
        return self.storage[ip]

    def decode_execute(self, instruction: str):
        instruction = instruction.split()
        if instruction[0] == "noop":
            self._noop()
        elif instruction[0] == "addx":
            self._addx(int(instruction[1]))

    def _noop(self):
        self.store_signal()
        self.IP += 1

    def _addx(self, arg1: int):
        self.store_signal()
        if self.step_count == 0:
            self.step_count += 1
        else:
            self.step_count = 0
            self.IP += 1
            self.X += arg1

    def __repr__(self):
        return f"IP:{self.IP}\tX:{self.X}\tcycle:{self.cycle}"


def solve_part1(entries):
    debug_cycles = [20, 60, 100, 140, 180, 220]
    cpu = CPU(entries, debug_cycles)
    cpu.run()
    print(cpu.signal_strengths)
    return sum(cpu.signal_strengths)


def solve_part2(entries):
    cpu = CPU(entries, crt=CRT())
    cpu.run()
    return cpu.crt.__repr__()


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day10/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
