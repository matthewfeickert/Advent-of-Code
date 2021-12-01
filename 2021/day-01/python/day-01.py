#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def count_increases(inputs):
    return sum(inputs[step] > inputs[step - 1] for step in range(len(inputs)))


def test_part_one():
    assert count_increases(test_data) == 7


def part_one():
    inputs = load_input_file("../input.txt")
    answer = count_increases(inputs)
    print(f"\n# Measurements larger than the previous measurement: {answer}")


# def test_part_two():
#     assert product_of_ntuples(test_data, 2020, 3) == 241861950


# def part_two():
#     inputs = load_input_file("input.txt")
#     answer = product_of_ntuples(inputs, target=2020, order=3)
#     print(f"\n# Product of tripplet is: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
