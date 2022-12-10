from aoc2022.util import get_input


class Knot:
    def __init__(self, id: int = None, x: int = 0, y: int = 0):
        self.id = id
        self.x = x
        self.y = y
        self.prev: Knot = None
        self.next: Knot = None

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

    def __repr__(self):
        return f"Knot{self.id, (self.x,self.y)}"


class Rope:
    def __init__(self, head: Knot):
        self.head = head
        self.tail_visited: set = set()

    def get_tail(self) -> Knot:
        *_, tail = self.knot_generator()
        return tail

    def add_knot(self, new_knot: Knot):
        tail = self.get_tail()
        tail.next = new_knot

    def move_head(self, command):
        movement = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }
        direction, count = command.split()
        print(f"move head {direction} x{count}")
        for _ in range(int(count)):
            change = movement[direction]
            self.head.move(change)
            for knot in self.knot_generator():
                if knot.next is not None and not knot.touching(knot.next):
                    self.move_next(knot)
                    knot = knot.next
                else:
                    break
            self.tail_visited.add(self.get_tail().get_location())

    def move_next(self, knot: Knot):
        if knot.y == knot.next.y:  # same row
            if knot.x > knot.next.x:
                knot.next.move((1, 0))  # move right
            else:
                knot.next.move((-1, 0))  # mvoe left
        elif knot.x == knot.next.x:  # same column
            if knot.y > knot.next.y:
                knot.next.move((0, 1))  # move up
            else:
                knot.next.move((0, -1))  # move down
        else:  # diagonal difference
            if knot.y > knot.next.y and knot.x > knot.next.x:
                knot.next.move((1, 1))  # move up and right
            elif knot.y > knot.next.y and knot.x < knot.next.x:
                knot.next.move((-1, 1))  # move up and left
            elif knot.y < knot.next.y and knot.x > knot.next.x:
                knot.next.move((1, -1))  # move down and right
            else:
                knot.next.move((-1, -1))  # move down and left

    def knot_generator(self):
        knot = self.head
        while knot.next is not None:
            yield knot
            knot = knot.next
        yield knot

    def __repr__(self):
        result = list()
        [result.append(knot) for knot in self.knot_generator()]
        return f"Rope:{str(result)}"


def solve_part1(entries):
    rope = Rope(Knot(id=1))
    rope.add_knot(Knot(id=2))
    for movement in entries:
        rope.move_head(movement)
        print(rope)
    return len(rope.tail_visited)


def solve_part2(entries):
    rope = Rope(Knot(id=1))
    for i in range(1, 10):
        rope.add_knot(Knot(id=i))
    for movement in entries:
        rope.move_head(movement)
        print(rope)
    return len(rope.tail_visited)


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day09/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
