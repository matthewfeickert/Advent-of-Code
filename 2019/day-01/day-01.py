#!/usr/bin/env python3
import numpy as np
import csv


def load_input_file(path):
    return [int(x[0]) for x in csv.reader(open(path, "r"), delimiter="\t")]


def fuel_for_module(mass):
    return np.floor(mass / 3.0) - 2.0


def test_fuel():
    assert fuel_for_module(12) == 2
    assert fuel_for_module(14) == 2
    assert fuel_for_module(1969) == 654
    assert fuel_for_module(100756) == 33583


def part_one():
    inputs = load_input_file("input.txt")
    # Answer is desired as an int
    sum_of_fuel = int(fuel_for_module(np.array(inputs)).sum())
    print(f"\n# Total mass: {sum_of_fuel}\n")


def total_fuel_required(mass):
    total_fuel = 0

    remaining_mass = fuel_for_module(mass)
    while remaining_mass > 0:
        total_fuel += remaining_mass
        remaining_mass = fuel_for_module(remaining_mass)

    return total_fuel


def test_total_fuel():
    assert total_fuel_required(14) == 2
    assert total_fuel_required(1969) == 966
    assert total_fuel_required(100756) == 50346


def part_two():
    inputs = load_input_file("input.txt")
    sum_of_fuel = int(sum(total_fuel_required(mass) for mass in inputs))
    print(f"# Total mass with fuel: {sum_of_fuel}\n")


def tests():
    test_fuel()
    test_total_fuel()


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    tests()
    main()
