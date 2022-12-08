from dataclasses import dataclass
from anytree import Node, RenderTree
from aoc2022.util import get_input


def build_tree(entries):
    root = Node(name="root", node_type="directory", size=0)
    current_directory_node = root
    for line in entries:
        line = line.split()
        if line[0] == "$":  # command
            command = line[1]
            if command == "cd":
                if line[2] == "/":  # skip special root case
                    pass
                elif line[2] == "..":  # return to parent directory
                    current_directory_node = current_directory_node.parent
                else:  # create and change to sub directory
                    subdir_node = Node(
                        name=line[2],
                        parent=current_directory_node,
                        node_type="directory",
                        size=0,
                    )
                    current_directory_node = subdir_node
            elif command == "ls":
                pass
            else:
                raise KeyError(f"Unable to parse command {command}")
        elif line[0] == "dir":
            pass
        else:  # file
            size = int(line[0])
            filename = line[1]
            Node(
                name=filename,
                parent=current_directory_node,
                node_type="file",
                size=size,
            )
    return root


def solve_part1(entries):
    result = 0
    filesystem = build_tree(entries)
    for node in filesystem.descendants:
        if node.node_type == "directory":
            value = sum([leaf.size for leaf in node.leaves])
            if value <= 100000:
                result += value
    return result


def solve_part2(entries):
    total_space = 70000000
    needed_space = 30000000
    filesystem = build_tree(entries)
    total_used = sum(leaf.size for leaf in filesystem.leaves)
    total_free = total_space - total_used
    to_free = needed_space - total_free
    potential_directories = []
    for node in filesystem.descendants:
        if node.node_type == "directory":
            value = sum([leaf.size for leaf in node.leaves])
            if value >= to_free:
                potential_directories.append((node, value))
    target_directory = min(potential_directories, key=lambda t: t[1])
    return target_directory[1]


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day07/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
