#!/usr/bin/env python3

import numpy as np

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


def count_trees(data, horizontal_shift, vertical_shift, target="#"):
    cycle_length = len(data[0])
    cycle_postion = 0
    tree_list = []
    for row in data[1::vertical_shift]:
        cycle_postion = (cycle_postion + horizontal_shift) % cycle_length
        tree_list.append(row[cycle_postion])
    return tree_list.count(target)


def test_part_one():
    test_data = load_input_file("test_data.txt")
    tree_count = count_trees(
        test_data, horizontal_shift=3, vertical_shift=1, target="#"
    )
    assert tree_count == 7


def part_one():
    inputs = load_input_file("input.txt")
    tree_count = count_trees(inputs, horizontal_shift=3, vertical_shift=1, target="#")
    print(f"\n# Number of trees encountered: {tree_count}")


def test_part_two():
    test_data = load_input_file("test_data.txt")
    shift_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = []
    for shifts in shift_list:
        tree_counts.append(
            count_trees(
                test_data,
                horizontal_shift=shifts[0],
                vertical_shift=shifts[1],
                target="#",
            )
        )
    assert np.prod(tree_counts) == 336


def part_two():
    inputs = load_input_file("input.txt")
    shift_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = []
    for shifts in shift_list:
        tree_counts.append(
            count_trees(
                inputs,
                horizontal_shift=shifts[0],
                vertical_shift=shifts[1],
                target="#",
            )
        )
    answer = np.prod(tree_counts)
    print(tree_counts)
    print(f"\n# Product of trees encountered: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
