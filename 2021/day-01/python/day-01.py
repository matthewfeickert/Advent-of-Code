#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def count_increases(inputs):
    return sum(inputs[step] > inputs[step - 1] for step in range(len(inputs)))


def sliding_window_count(inputs, width=3):
    sum_list = [
        sum(inputs[step : step + width])  # noqa: E203
        for step in range(len(inputs) - (width - 1))
    ]

    return sum(sum_list[step] > sum_list[step - 1] for step in range(len(sum_list)))


def test_part_one():
    assert count_increases(test_data) == 7


def part_one():
    inputs = load_input_file("../input.txt")
    answer = count_increases(inputs)
    print(f"\n# Measurements larger than the previous measurement: {answer}")


def test_part_two():
    assert sliding_window_count(test_data) == 5


def part_two():
    inputs = load_input_file("../input.txt")
    answer = sliding_window_count(inputs, width=3)
    print(f"\n# Sums larger than the previous sum: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
