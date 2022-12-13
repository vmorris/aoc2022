from aoc2022.util import get_input

# Check if cell (x, y) is valid or not
def is_valid_cell(x, y, cells):
    try:
        cell = cells[y][x]
    except IndexError:
        return False
    return True


def find_paths_util(maze, source, destination, visited, path, paths):
    """Find paths using Breadth First Search algorith"""
    # Done if destination is found
    if source == destination:
        paths.append(path[:])  # append copy of current path
        return

    # mark current cell as visited
    N = len(maze)
    x, y = source
    visited[y][x] = True

    # if current cell is a valid and open cell,
    if is_valid_cell(x, y, N) and maze[y][x]:
        # Using Breadth First Search on path extension in all direction

        # go right (x, y) --> (x + 1, y)
        if x + 1 < N and (not visited[x + 1][y]):
            path.append((x + 1, y))
            find_paths_util(maze, (x + 1, y), destination, visited, path, paths)
            path.pop()

        # go left (x, y) --> (x - 1, y)
        if x - 1 >= 0 and (not visited[x - 1][y]):
            path.append((x - 1, y))
            find_paths_util(maze, (x - 1, y), destination, visited, path, paths)
            path.pop()

        # go up (x, y) --> (x, y + 1)
        if y + 1 < N and (not visited[x][y + 1]):
            path.append((x, y + 1))
            find_paths_util(maze, (x, y + 1), destination, visited, path, paths)
            path.pop()

        # go down (x, y) --> (x, y - 1)
        if y - 1 >= 0 and (not visited[x][y - 1]):
            path.append((x, y - 1))
            find_paths_util(maze, (x, y - 1), destination, visited, path, paths)
            path.pop()

        # Unmark current cell as visited
    visited[x][y] = False

    return paths


def find_paths(maze, source, destination):
    """Sets up and searches for paths"""
    N = len(maze)  # size of Maze is N x N

    # 2D matrix to keep track of cells involved in current path
    visited = [[False] * N for _ in range(N)]

    path = [source]
    paths = []
    paths = find_paths_util(maze, source, destination, visited, path, paths)

    return paths


def solve_part1(entries):
    print(get_destination(entries))
    print(len(entries))
    print(len(entries[0]))
    return


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day12/input", "char-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
