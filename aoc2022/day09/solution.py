from aoc2022.util import get_input
from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int

    def move(self, change):
        self.x += change[0]
        self.y += change[1]

    def get_location(self):
        return (self.x, self.y)

    def touching(self, other):
        x_touching = False
        y_touching = False
        if abs(self.x - other.x) <= 1:
            x_touching = True
        if abs(self.y - other.y) <= 1:
            y_touching = True
        return x_touching and y_touching


@dataclass
class World:
    head: Point = field(init=False)
    tail: Point = field(init=False)
    tail_visited: set = field(default_factory=set, repr=False)

    def __post_init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        self.tail_visited.add(self.tail.get_location())

    def move_head(self, command):
        movement = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }
        direction, count = command.split()
        for _ in range(int(count)):
            change = movement[direction]
            self.head.move(change)
            if not self.head.touching(self.tail):
                self.move_tail()

    def move_tail(self):
        if self.head.y == self.tail.y:  # same row
            if self.head.x > self.tail.x:
                self.tail.x += 1  # move right
            else:
                self.tail.x -= 1  # mvoe left
        elif self.head.x == self.tail.x:  # same column
            if self.head.y > self.tail.y:
                self.tail.y += 1  # move up
            else:
                self.tail.y -= 1  # move down
        else:  # diagonal difference
            if self.head.y > self.tail.y and self.head.x > self.tail.x:
                # move up and right
                self.tail.y += 1
                self.tail.x += 1
            elif self.head.y > self.tail.y and self.head.x < self.tail.x:
                # move up and left
                self.tail.y += 1
                self.tail.x -= 1
            elif self.head.y < self.tail.y and self.head.x > self.tail.x:
                # move down and right
                self.tail.y -= 1
                self.tail.x += 1
            else:
                # move down and left
                self.tail.y -= 1
                self.tail.x -= 1
        self.tail_visited.add(self.tail.get_location())
        assert self.head.touching(self.tail)


def solve_part1(entries):
    w = World()
    for movement in entries:
        w.move_head(movement)
    return len(w.tail_visited)


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day09/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
