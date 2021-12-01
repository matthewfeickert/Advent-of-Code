#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def count_increases(inputs, width=1):
    return sum(
        inputs[step] > inputs[step - width] for step in range(width, len(inputs))
    )


def test_part_one():
    assert count_increases(test_data, width=1) == 7


def part_one():
    inputs = load_input_file("input.txt")
    answer = count_increases(inputs, width=1)
    print(f"\n# Measurements larger than the previous measurement: {answer}")


def test_part_two():
    assert count_increases(test_data, width=3) == 5


def part_two():
    inputs = load_input_file("input.txt")
    answer = count_increases(inputs, width=3)
    print(f"\n# Sums larger than the previous sum: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
