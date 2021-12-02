#!/usr/bin/env python3


def process_input(input):
    data = [line.split(" ") for line in input.splitlines()]
    return [(entry[0], int(entry[1])) for entry in data]


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2\
"""
test_data = process_input(test_string)


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


def calculate_aim_posiiton(inputs):
    horizontal = 0
    depth = 0
    aim = 0

    for direction, value in inputs:
        if direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
        else:
            horizontal += value
            depth += aim * value

    return horizontal, depth


def test_part_two():
    horizontal, depth = calculate_aim_posiiton(test_data)
    assert horizontal, depth == (15, 60)
    assert horizontal * depth == 900


def part_two():
    inputs = load_input_file("input.txt")
    horizontal, depth = calculate_aim_posiiton(inputs)
    answer = horizontal * depth
    print(f"\n# Product of final horizontal position and final depth: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
