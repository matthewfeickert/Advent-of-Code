#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_common_element(word_0, word_1):
    return "".join(set(word_0).intersection(word_1))


def get_priority(inputs):
    half_length = len(inputs) // 2
    left, right = inputs[:half_length], inputs[half_length:]
    common_element = get_common_element(left, right)

    offset = 0 if common_element.islower() else 26
    return ord(common_element.lower()) - 96 + offset


def compare_three(inputs):
    word_0, word_1, word_2 = inputs
    common_element = get_common_element(get_common_element(word_0, word_1), word_2)

    offset = 0 if common_element.islower() else 26
    return ord(common_element.lower()) - 96 + offset


def test_part_one():
    inputs = load_input_file("test_input.txt")
    priorities = [get_priority(x) for x in inputs]
    assert priorities == [16, 38, 42, 22, 20, 19]
    assert sum(priorities) == 157


def part_one():
    inputs = load_input_file("input.txt")
    priorities = [get_priority(x) for x in inputs]
    answer = sum(priorities)
    print(f"\n# Sum of the priorities of the common items: {answer}")


def test_part_two():
    inputs = load_input_file("test_input.txt")
    step = 3
    strides = [inputs[x : x + step] for x in range(0, len(inputs), step)]
    priorities = [compare_three(x) for x in strides]
    assert priorities == [18, 52]
    assert sum(priorities) == 70


def part_two():
    inputs = load_input_file("input.txt")
    step = 3
    strides = [inputs[x : x + step] for x in range(0, len(inputs), step)]
    priorities = [compare_three(x) for x in strides]
    answer = sum(priorities)
    print(f"\n# Sum of the priorities of the common items: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
