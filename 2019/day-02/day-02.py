#!/usr/bin/env python3
import csv
import itertools


def load_input_file(path):
    # Load a single line csv file
    return [list(map(int, rec)) for rec in csv.reader(open(path), delimiter=",")][
        0
    ]


def sum_op(list, idx):
    list[list[idx + 3]] = list[list[idx + 1]] + list[list[idx + 2]]
    return list


def prod_op(list, idx):
    list[list[idx + 3]] = list[list[idx + 1]] * list[list[idx + 2]]
    return list


def test_sum_op():
    test_list = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    target_list = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert sum_op(test_list, 0) == target_list


def test_prod_op():
    test_list = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    target_list = [
        3500,
        9,
        10,
        70,
        2,
        3,
        11,
        0,
        99,
        30,
        40,
        50,
    ]
    assert prod_op(test_list, 4) == target_list


def intcode(list, noun=None, verb=None):
    list = list[:]
    if noun:
        list[1] = noun
    if verb:
        list[2] = verb
    list_len = len(list)
    idx = 0
    while idx < list_len:
        if list[idx] == 1:
            list = sum_op(list, idx)
        elif list[idx] == 2:
            list = prod_op(list, idx)
        elif list[idx] == 99:
            break
        idx = idx + 4
    return list


def test_intcode():
    assert intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def tests():
    test_sum_op()
    test_prod_op()
    test_intcode()


def part_one():
    input = load_input_file("input.txt")
    # reset to "1202 program alarm" state
    output = intcode(input, 12, 2)
    print(f"\n# position 0 after program halt: {output[0]}\n")
    return 0


def part_two():
    input = load_input_file("input.txt")
    # Brute force the solution
    target = 19690720
    search_range = 100
    for noun, verb in itertools.product(range(search_range), range(search_range)):
        if intcode(input, noun, verb)[0] == target:
            print(f"# noun verb inputs are: {noun}, {verb}\n")
            print(f"  100 * noun + verb = {100 * noun + verb}")
            break


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    tests()
    main()
