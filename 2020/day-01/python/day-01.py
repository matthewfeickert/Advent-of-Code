#!/usr/bin/env python3
from itertools import combinations
from functools import reduce
from operator import mul


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


def test_data():
    return [1721, 979, 366, 299, 675, 1456]


def product_of_ntuples(inputs, target, order):
    # https://docs.python.org/3/library/itertools.html#itertools.combinations
    for ntuple in combinations(inputs, order):
        if sum(ntuple) == target:
            return reduce(mul, ntuple)


def test_part_one():
    assert product_of_ntuples(test_data(), 2020, 2) == 514579


def part_one():
    inputs = load_input_file("input.txt")
    answer = product_of_ntuples(inputs, 2020, 2)
    print(f"\n# Product of pair is: {answer}")


def test_part_two():
    assert product_of_ntuples(test_data(), 2020, 3) == 241861950


def part_two():
    inputs = load_input_file("input.txt")
    answer = product_of_ntuples(inputs, target=2020, order=3)
    print(f"\n# Product of tripplet is: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
