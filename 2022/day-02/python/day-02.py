#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip().split(" ") for line in input_file]


def play_game(inputs):
    # Rock: A,X, 1 point
    # Paper: B,Y, 2 points
    # Scissors: C,Z, 3 points

    # lose: 0
    # draw: 3
    # win: 6
    opponent_move, your_move = inputs

    shape_points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    shape_score = shape_points[your_move]

    if shape_points[opponent_move] == shape_score:
        return 3 + shape_score

    if opponent_move == "A":
        return 0 + shape_score if your_move == "Z" else 6 + shape_score
    if opponent_move == "B":
        return 0 + shape_score if your_move == "X" else 6 + shape_score
    if opponent_move == "C":
        return 0 + shape_score if your_move == "Y" else 6 + shape_score


def play_game_second_round(inputs):
    # Rock: A, 1 point
    # Paper: B, 2 points
    # Scissors: C, 3 points

    # Lose: X, 0 points
    # Draw: Y, 3 points
    # Win: Z, 6 points

    opponent_move, goal = inputs

    if goal == "X":
        lose_dict = {"A": "C", "B": "A", "C": "B"}
        your_move = lose_dict[opponent_move]
    elif goal == "Y":
        your_move = opponent_move
    if goal == "Z":
        win_dict = {"A": "B", "B": "C", "C": "A"}

        your_move = win_dict[opponent_move]

    conversion_dict = {"A": "X", "B": "Y", "C": "Z"}

    return play_game([opponent_move, conversion_dict[your_move]])


def test_part_one():
    inputs = load_input_file("test_input.txt")
    scores = [play_game(x) for x in inputs]
    assert scores == [8, 1, 6]
    assert sum(scores) == 15


def part_one():
    inputs = load_input_file("input.txt")
    scores = [play_game(x) for x in inputs]
    answer = sum(scores)
    print(f"\n# Total score given strategy guide: {answer}")


def test_part_two():
    inputs = load_input_file("test_input.txt")
    scores = [play_game_second_round(x) for x in inputs]
    assert scores == [4, 1, 7]
    assert sum(scores) == 12


def part_two():
    inputs = load_input_file("input.txt")
    scores = [play_game_second_round(x) for x in inputs]
    answer = sum(scores)
    print(f"\n# Total score given strategy guide: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
