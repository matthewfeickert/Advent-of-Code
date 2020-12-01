#!/usr/bin/env python3
import numpy as np
import csv
import itertools
from functools import reduce
from operator import mul


def load_input_file(path):
    return [int(x[0]) for x in csv.reader(open(path, "r"), delimiter="\t")]


def product_of_summands(inputs, target):
    for pair in itertools.product(inputs, inputs[1:]):
        if sum(pair) == target:
            return reduce(mul, pair)


def part_one():
    inputs = load_input_file("input.txt")
    print(np.array(inputs))
    answer = product_of_summands(inputs, 2020)
    print(f"\n# Product is: {answer}\n")


# def tests():
#     test_fuel()
#     test_total_fuel()


def main():
    part_one()
    # part_two()


if __name__ == "__main__":
    # tests()
    main()
