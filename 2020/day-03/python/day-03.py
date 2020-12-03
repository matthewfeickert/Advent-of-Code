#!/usr/bin/env python3
# Faster than NumPy for small lists
from functools import reduce
from operator import mul


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


test_data = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#\
"""


def count_trees(data, horiz_shift, vert_shift, target="#"):
    cycle_length = len(data[0])
    cycle_postion = 0
    tree_list = []
    for row in data[vert_shift::vert_shift]:
        cycle_postion = (cycle_postion + horiz_shift) % cycle_length
        tree_list.append(row[cycle_postion])
    return tree_list.count(target)


def test_part_one():
    tree_count = count_trees(test_data.split(), horiz_shift=3, vert_shift=1)
    assert tree_count == 7


def part_one():
    inputs = load_input_file("input.txt")
    tree_count = count_trees(inputs, horiz_shift=3, vert_shift=1)
    print(f"\n# Number of trees encountered: {tree_count}")


def test_part_two():
    shift_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = [
        count_trees(
            test_data.split(),
            horiz_shift=h_shift,
            vert_shift=v_shift,
        )
        for h_shift, v_shift in shift_list
    ]
    assert tree_counts == [2, 7, 3, 4, 2]
    assert reduce(mul, tree_counts) == 336


def part_two():
    inputs = load_input_file("input.txt")
    shift_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = [
        count_trees(
            inputs,
            horiz_shift=h_shift,
            vert_shift=v_shift,
        )
        for h_shift, v_shift in shift_list
    ]
    answer = reduce(mul, tree_counts)
    print(f"\n# Product of trees encountered: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
