from aoc2022.util import get_input

import logging

# logging.getLogger().setLevel(logging.DEBUG)


def solve_part1(entries):
    x_length = len(entries[0])
    y_length = len(entries)
    perimeter_count = (2 * x_length) + (2 * y_length) - 4
    interior_count = 0
    for y_index, row in enumerate(entries[1 : len(entries) - 1]):
        y_index += 1
        for x_index, tree in enumerate(row[1 : len(row) - 1]):
            x_index += 1
            logging.debug(f"{x_index},{y_index}: {tree}")
            # check left visibility
            if max(entries[y_index][0:x_index]) < tree:
                logging.debug("left visible")
                interior_count += 1
                continue
            # check right visibility
            if max(entries[y_index][x_index + 1 :]) < tree:
                logging.debug("right visible")
                interior_count += 1
                continue
            # check top visibility
            to_check = []
            for i in range(y_index - 1, -1, -1):
                to_check.append(entries[i][x_index])
            if max(to_check) < tree:
                logging.debug("top visible")
                interior_count += 1
                continue
            # check bottom visibility
            to_check = []
            for i in range(y_index + 1, y_length):
                to_check.append(entries[i][x_index])
            if max(to_check) < tree:
                logging.debug("botton visible")
                interior_count += 1
                continue
    return interior_count + perimeter_count


def solve_part2(entries):
    y_length = len(entries)
    highest_score = 0
    for y_index, row in enumerate(entries[1 : len(entries) - 1]):
        y_index += 1
        for x_index, tree in enumerate(row[1 : len(row) - 1]):
            scenic_score = 1
            x_index += 1
            logging.debug(f"{x_index},{y_index}: {tree}")
            # count left
            logging.debug("looking left...")
            count = 0
            for i in entries[y_index][x_index - 1 :: -1]:
                logging.debug(f"checking {i}")
                if i < tree:
                    count += 1
                elif i >= tree:
                    logging.debug(f"found blocking tree: {i}")
                    count += 1
                    break
            logging.debug(f"count: {count}")
            scenic_score *= count
            # count right
            logging.debug("looking right...")
            count = 0
            for i in entries[y_index][x_index + 1 : len(row)]:
                logging.debug(f"checking {i}")
                if i < tree:
                    count += 1
                elif i >= tree:
                    logging.debug(f"found blocking tree: {i}")
                    count += 1
                    break
            logging.debug(f"count: {count}")
            scenic_score *= count
            # count top
            logging.debug("looking top...")
            count = 0
            to_check = []
            for i in range(y_index - 1, -1, -1):
                to_check.append(entries[i][x_index])
            for i in to_check:
                logging.debug(f"checking {i}")
                if i < tree:
                    count += 1
                elif i >= tree:
                    logging.debug(f"found blocking tree: {i}")
                    count += 1
                    break
            logging.debug(f"count: {count}")
            scenic_score *= count
            # count bottom
            logging.debug("looking bottom...")
            count = 0
            to_check = []
            for i in range(y_index + 1, y_length):
                to_check.append(entries[i][x_index])
            for i in to_check:
                logging.debug(f"checking {i}")
                if i < tree:
                    count += 1
                elif i >= tree:
                    logging.debug(f"found blocking tree: {i}")
                    count += 1
                    break
            logging.debug(f"count: {count}")
            scenic_score *= count
            logging.debug(f"scenic score: {scenic_score}")
            if scenic_score > highest_score:
                logging.debug(f"new highscore: {scenic_score}")
                highest_score = scenic_score
    return highest_score


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day08/input", type="int-matrix")
    print(solve_part1(entries))
    print(solve_part2(entries))
