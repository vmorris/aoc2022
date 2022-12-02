from aoc2022.util import get_input


def calculate_score_round1(round):
    opponent_play = round[0]
    self_play = round[1]
    result = 0
    if self_play == "X":
        # I play Rock....
        result = 1
        if opponent_play == "A":  # Rock
            result += 3  # Draw
        elif opponent_play == "B":  # Paper
            result += 0  # Lose
        elif opponent_play == "C":  # Scissors
            result += 6  # Win
    elif self_play == "Y":
        # I play Paper ...
        result = 2
        if opponent_play == "A":  # Rock
            result += 6  # Win
        elif opponent_play == "B":  # Paper
            result += 3  # Draw
        elif opponent_play == "C":  # Scissors
            result += 0  # Lose
    elif self_play == "Z":
        # I play Scissors....
        result = 3
        if opponent_play == "A":  # Rock
            result += 0  # Lose
        elif opponent_play == "B":  # Paper
            result += 6  # Win
        elif opponent_play == "C":  # Scissors
            result += 3  # Draw
    return result


def solve_part1(entries):
    total = 0
    for entry in entries:
        total += calculate_score_round1(entry)
    return total


def calculate_score_round2(round):
    opponent_play = round[0]
    win_lose_draw = round[1]
    result = 0
    if opponent_play == "A":
        # They play Rock ...
        if win_lose_draw == "X":  # Lose
            result += 0
            result += 3  # I play Scissors
        elif win_lose_draw == "Y":  # Draw
            result += 3
            result += 1  # I play Rock
        elif win_lose_draw == "Z":  # Win
            result += 6
            result += 2  # I play Paper
    elif opponent_play == "B":
        # They play Paper ...
        if win_lose_draw == "X":  # Lose
            result += 0
            result += 1  # I play Rock
        elif win_lose_draw == "Y":  # Draw
            result += 3
            result += 2  # I play Paper
        elif win_lose_draw == "Z":  # Win
            result += 6
            result += 3  # I play Scissors
    elif opponent_play == "C":
        # They play Sciscors ...
        if win_lose_draw == "X":  # Lose
            result += 0
            result += 2  # I play Paper
        elif win_lose_draw == "Y":  # Draw
            result += 3
            result += 3  # I play Scissors
        elif win_lose_draw == "Z":  # Win
            result += 6
            result += 1  # I play Rock
    return result


def solve_part2(entries):
    total = 0
    for entry in entries:
        total += calculate_score_round2(entry)
    return total


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2022/day2/input", type="split")
    print(solve_part1(entries))
    print(solve_part2(entries))
