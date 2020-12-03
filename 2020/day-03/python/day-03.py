#!/usr/bin/env python3

# import numpy as np

# Notes:
# Open: .
# Tree: #

# Slope: right 3, down 1


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


# test_data = """\
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#\
# """


def count_trees(data, shift, target="#"):
    cycle_length = len(data[0])
    cycle_postion = 0
    tree_list = []
    for row in data[1:]:
        cycle_postion = (cycle_postion + shift) % cycle_length
        tree_list.append(row[cycle_postion])
    return tree_list.count(target)


def test_part_one():
    test_data = load_input_file("test_data.txt")
    tree_count = count_trees(test_data, shift=3, target="#")
    assert tree_count == 7


def part_one():
    inputs = load_input_file("input.txt")
    tree_count = count_trees(inputs, shift=3, target="#")
    print(f"\n# Number of trees encountered: {tree_count}")


def test_part_two():
    pass


def part_two():
    # inputs = load_input_file("input.txt")
    # print(f"\n# Answer: {answer}")
    pass


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
