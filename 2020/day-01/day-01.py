#!/usr/bin/env python3
import csv
from itertools import product
from itertools import combinations
from functools import reduce
from operator import mul


def load_input_file(path):
    return [int(x[0]) for x in csv.reader(open(path, "r"), delimiter="\t")]


def test_data():
    return [1721, 979, 366, 299, 675, 1456]


def product_of_summands(inputs, target):
    for pair in product(inputs, inputs[1:]):
        if sum(pair) == target:
            return reduce(mul, pair)


def test_pairs():
    assert product_of_summands(test_data(), 2020) == 514579


def product_of_ntuples(inputs, target, order):
    """
    https://docs.python.org/3/library/itertools.html#itertools.combinations
    """
    for ntuple in combinations(inputs, order):
        if sum(ntuple) == target:
            return reduce(mul, ntuple)


def test_tripples():
    assert product_of_ntuples(test_data(), 2020, 3) == 241861950


def part_one():
    inputs = load_input_file("input.txt")
    answer = product_of_summands(inputs, 2020)
    print(f"\n# Product of pair is: {answer}")


def part_two():
    inputs = load_input_file("input.txt")
    answer = product_of_ntuples(inputs, target=2020, order=3)
    print(f"\n# Product of tripplet is: {answer}")


def tests():
    test_pairs()
    test_tripples()


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    tests()
    main()
