#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip().split(",") for line in input_file]


def range_subset(pair):
    ranges = [range(*x) for x in pair]
    if ranges[0] == ranges[1]:
        return True
    if len(ranges[0]) > 0 and len(ranges[1]) > 0:
        return (
            True
            if ranges[0].start in ranges[1] and ranges[0].stop in ranges[1]
            else ranges[1].start in ranges[0] and ranges[1].stop in ranges[0]
        )

    zero_range = ranges[[len(x) > 0 for x in ranges].index(False)]
    full_range = ranges[[len(x) > 0 for x in ranges].index(True)]
    return zero_range.start in {full_range.start, full_range.stop}


def test_part_one():
    inputs = load_input_file("test_input.txt")

    _new_inputs = [
        [tuple(int(x) for x in group.split("-")) for group in assignment]
        for assignment in inputs
    ]
    inputs = _new_inputs

    contained_pairs = []
    pair_counter = 0
    for pair in inputs:
        set_0, set_1 = pair
        a, b = set_0
        c, d = set_1

        if a <= c <= d <= b:
            pair_counter += 1
            contained_pairs.append(pair)
        elif c <= a <= b <= d:
            pair_counter += 1
            contained_pairs.append(pair)

    assert pair_counter == 2
    assert contained_pairs == [[(2, 8), (3, 7)], [(6, 6), (4, 6)]]


def part_one():
    inputs = load_input_file("input.txt")

    _new_inputs = [
        [tuple(int(x) for x in group.split("-")) for group in assignment]
        for assignment in inputs
    ]
    inputs = _new_inputs

    contained_pairs = []
    pair_counter = 0
    for pair in inputs:
        set_0, set_1 = pair
        a, b = set_0
        c, d = set_1

        if a <= c <= d <= b:
            pair_counter += 1
            contained_pairs.append(pair)
        elif c <= a <= b <= d:
            pair_counter += 1
            contained_pairs.append(pair)

    answer = pair_counter
    print(f"\n# Assignment pairs with one range fully contained in the other: {answer}")


# def test_part_two():
#     inputs = load_input_file("test_input.txt")
#     step = 3
#     strides = [inputs[x : x + step] for x in range(0, len(inputs), step)]
#     priorities = [compare_three(x) for x in strides]
#     assert priorities == [18, 52]
#     assert sum(priorities) == 70


# def part_two():
#     inputs = load_input_file("input.txt")
#     step = 3
#     strides = [inputs[x : x + step] for x in range(0, len(inputs), step)]
#     priorities = [compare_three(x) for x in strides]
#     answer = sum(priorities)
#     print(f"\n# Sum of the priorities of the common items: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
