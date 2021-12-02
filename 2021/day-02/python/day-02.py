#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        data = [line.strip().split(" ") for line in input_file]
        return [(entry[0], int(entry[1])) for entry in data]


test_string = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2\
"""
test_data = [line.split(" ") for line in test_string.split("\n")]
test_data = [(entry[0], int(entry[1])) for entry in test_data]


def calculate_position(inputs):
    horizontal = 0
    depth = 0
    for direction, distance in inputs:
        if direction == "down":
            depth += distance
        elif direction == "forward":
            horizontal += distance
        else:
            depth -= distance
    return horizontal, depth


def test_part_one():
    horizontal, depth = calculate_position(test_data)
    assert horizontal, depth == (15, 10)
    assert horizontal * depth == 150


def part_one():
    inputs = load_input_file("input.txt")
    horizontal, depth = calculate_position(inputs)
    answer = horizontal * depth
    print(f"\n# Product of final horizontal position and final depth: {answer}")


# def test_part_two():
#     assert count_increases(test_data, width=3) == 5


# def part_two():
#     inputs = load_input_file("input.txt")
#     answer = count_increases(inputs, width=3)
#     print(f"\n# Sums larger than the previous sum: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
