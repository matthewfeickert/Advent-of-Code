#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


test_data = [None]


def test_part_one():
    pass


def part_one():
    inputs = load_input_file("input.txt")
    # answer = product_of_ntuples(inputs, 2020, 2)
    answer = None
    print(f"\n# Product of pair is: {answer}")


def test_part_two():
    pass


def part_two():
    pass


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
