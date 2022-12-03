#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_priority(inputs):
    half_length = len(inputs) // 2
    left, right = inputs[:half_length], inputs[half_length:]
    common_element = "".join(set(left).intersection(right))

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
    scores = [play_game_second_round(x) for x in inputs]
    assert scores == [4, 1, 7]
    assert sum(scores) == 12


def part_two():
    inputs = load_input_file("input.txt")
    scores = [play_game_second_round(x) for x in inputs]
    answer = sum(scores)
    print(f"\n# Total score given strategy guide: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    # test_part_two()
    # part_two()
