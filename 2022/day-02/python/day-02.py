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


def part_two():
    inputs = load_input_file("input.txt")


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
