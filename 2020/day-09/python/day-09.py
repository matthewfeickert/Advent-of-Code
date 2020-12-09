from itertools import permutations


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


def find_invalid_number(inputs, preamble=None):
    for idx, item in enumerate(inputs[preamble:]):
        available = inputs[idx : idx + preamble]  # noqa: E203
        sum_of_pairs = [sum(pair) for pair in permutations(available, r=2)]
        if not inputs[idx + preamble] in sum_of_pairs:
            return inputs[idx + preamble]


def test_part_one():
    inputs = load_input_file("test_data.txt")
    answer = find_invalid_number(inputs, preamble=5)
    assert answer == 127


def part_one():
    inputs = load_input_file("input.txt")
    answer = find_invalid_number(inputs, preamble=25)
    print(f"\n# First number not in sums of preamble: {answer}")


def find_subrange(inputs, target):
    len_input = len(inputs)
    for start in range(len_input):
        for offset in range(len_input - start - 1):
            subrange = inputs[start : start + offset]  # noqa: E203
            if sum(subrange) == target:
                return subrange


def min_max_sum(data):
    return min(data) + max(data)


def test_part_two():
    inputs = load_input_file("test_data.txt")
    invalid_number = find_invalid_number(inputs, preamble=5)
    answer = min_max_sum(find_subrange(inputs, invalid_number))
    assert answer == 62


def part_two():
    inputs = load_input_file("input.txt")
    invalid_number = find_invalid_number(inputs, preamble=25)
    answer = min_max_sum(find_subrange(inputs, invalid_number))
    print(f"\n# Sum of min and max of subrange: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
