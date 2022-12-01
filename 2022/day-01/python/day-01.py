#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def filter_to_list(inputs):
    sublist = []
    full_list = []

    for idx, x in enumerate(inputs):
        if x != "" or idx + 1 == len(inputs):
            sublist.append(int(x))
            if idx + 1 == len(inputs):
                full_list.append(sublist)
        else:
            full_list.append(sublist)
            sublist = []
    return full_list


def test_part_one():
    inputs = load_input_file("test-input-01.txt")
    sum_list = filter_to_list(inputs)
    sum_list = list(map(sum, sum_list))
    assert max(sum_list) == 24000
    assert sum_list.index(max(sum_list)) == 3


def part_one():
    inputs = load_input_file("input.txt")
    sum_list = filter_to_list(inputs)
    answer = max(list(map(sum, sum_list)))
    print(f"\n# Total Calories: {answer}")


def test_part_two():
    assert count_increases(test_data, width=3) == 5


def part_two():
    inputs = load_input_file("input.txt")
    # answer = count_increases(inputs, width=3)
    # print(f"\n# Sums larger than the previous sum: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
