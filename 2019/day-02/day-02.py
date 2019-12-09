#!/usr/bin/env python3
import numpy as np
import csv


def convert_input(path):
    input = csv.reader(open(path, "r"), delimiter="\t")
    output = csv.writer(open("input.csv", "w"))
    output.writerows(input)
    # with csv.reader(open(path, "rb"), delimiter = '\t') as file:


def load_input_file(path):
    # return [int(x[0]) for x in csv.reader(open(path, "r"), delimiter=",")]
    # return list(csv.reader(open(path, "r"), delimiter=","))[0]
    return [list(map(int, rec)) for rec in csv.reader(open(path, "r"), delimiter=",")]
    # return list(csv.reader(open(path, "r"), delimiter=","))[0]


def sum_op(list, idx):
    list[list[idx + 3]] = list[list[idx + 1]] + list[list[idx + 2]]
    return list


def prod_op(list, idx):
    list[list[idx + 3]] = list[list[idx + 1]] * list[list[idx + 2]]
    return list


def apply_op(op, list, idx, offset=3):
    list[idx + offset] = op(list, idx)
    return list


def test_sum_op():
    test_list = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    assert sum_op(test_list, 0) == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_prod_op():
    test_list = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert prod_op(test_list, 4) == [
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
    # convert_input("input.txt")
    # input = load_input_file("input.csv")
    input = [
        1,
        0,
        0,
        3,
        1,
        1,
        2,
        3,
        1,
        3,
        4,
        3,
        1,
        5,
        0,
        3,
        2,
        1,
        10,
        19,
        1,
        6,
        19,
        23,
        1,
        10,
        23,
        27,
        2,
        27,
        13,
        31,
        1,
        31,
        6,
        35,
        2,
        6,
        35,
        39,
        1,
        39,
        5,
        43,
        1,
        6,
        43,
        47,
        2,
        6,
        47,
        51,
        1,
        51,
        5,
        55,
        2,
        55,
        9,
        59,
        1,
        6,
        59,
        63,
        1,
        9,
        63,
        67,
        1,
        67,
        10,
        71,
        2,
        9,
        71,
        75,
        1,
        6,
        75,
        79,
        1,
        5,
        79,
        83,
        2,
        83,
        10,
        87,
        1,
        87,
        5,
        91,
        1,
        91,
        9,
        95,
        1,
        6,
        95,
        99,
        2,
        99,
        10,
        103,
        1,
        103,
        5,
        107,
        2,
        107,
        6,
        111,
        1,
        111,
        5,
        115,
        1,
        9,
        115,
        119,
        2,
        119,
        10,
        123,
        1,
        6,
        123,
        127,
        2,
        13,
        127,
        131,
        1,
        131,
        6,
        135,
        1,
        135,
        10,
        139,
        1,
        13,
        139,
        143,
        1,
        143,
        13,
        147,
        1,
        5,
        147,
        151,
        1,
        151,
        2,
        155,
        1,
        155,
        5,
        0,
        99,
        2,
        0,
        14,
        0,
    ]
    # reset to "1202 program alarm" state
    output = intcode(input, 12, 2)
    print(f"\n# position 0 after program halt: {output[0]}\n")
    return 0


def part_two():
    input = [
        1,
        0,
        0,
        3,
        1,
        1,
        2,
        3,
        1,
        3,
        4,
        3,
        1,
        5,
        0,
        3,
        2,
        1,
        10,
        19,
        1,
        6,
        19,
        23,
        1,
        10,
        23,
        27,
        2,
        27,
        13,
        31,
        1,
        31,
        6,
        35,
        2,
        6,
        35,
        39,
        1,
        39,
        5,
        43,
        1,
        6,
        43,
        47,
        2,
        6,
        47,
        51,
        1,
        51,
        5,
        55,
        2,
        55,
        9,
        59,
        1,
        6,
        59,
        63,
        1,
        9,
        63,
        67,
        1,
        67,
        10,
        71,
        2,
        9,
        71,
        75,
        1,
        6,
        75,
        79,
        1,
        5,
        79,
        83,
        2,
        83,
        10,
        87,
        1,
        87,
        5,
        91,
        1,
        91,
        9,
        95,
        1,
        6,
        95,
        99,
        2,
        99,
        10,
        103,
        1,
        103,
        5,
        107,
        2,
        107,
        6,
        111,
        1,
        111,
        5,
        115,
        1,
        9,
        115,
        119,
        2,
        119,
        10,
        123,
        1,
        6,
        123,
        127,
        2,
        13,
        127,
        131,
        1,
        131,
        6,
        135,
        1,
        135,
        10,
        139,
        1,
        13,
        139,
        143,
        1,
        143,
        13,
        147,
        1,
        5,
        147,
        151,
        1,
        151,
        2,
        155,
        1,
        155,
        5,
        0,
        99,
        2,
        0,
        14,
        0,
    ]
    # run it all in reverse
    # start with the last 99 code and work backwards
    target = 19690720
    for noun in range(100):
        for verb in range(100):
            if intcode(input, noun, verb)[0] == target:
                print(f"\n# noun verb inputs are: {noun}, {verb}\n")
                print(f"100 * noun + verb = {100 * noun + verb}")
                break


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    tests()
    main()
