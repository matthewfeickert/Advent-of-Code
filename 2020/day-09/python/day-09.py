from itertools import permutations
from itertools import combinations


def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


test_data = [None]


def compute(inputs, preamble=None):
    for idx, item in enumerate(inputs[preamble:]):
        available = inputs[idx : idx + preamble]  # noqa: E203
        sum_of_pairs = [sum(pair) for pair in permutations(available, r=2)]
        if not inputs[idx + preamble] in sum_of_pairs:
            return inputs[idx + preamble]


def test_part_one():
    inputs = load_input_file("test_data.txt")
    answer = compute(inputs, preamble=5)
    assert answer == 127


def part_one():
    inputs = load_input_file("input.txt")
    answer = compute(inputs, preamble=25)
    print(f"\n# Answer: {answer}")


def find_subrange(inputs, target):
    idxs = list(range(len(inputs) + 1))
    contiguous_sublists = [inputs[i:j] for i, j in combinations(idxs, 2)]
    sublists = [list for list in contiguous_sublists if len(list) > 1]
    for sublist in sublists:
        if sum(sublist) == target:
            return min(sublist) + max(sublist)


def test_part_two():
    inputs = load_input_file("test_data.txt")
    invalid_number = compute(inputs, preamble=5)
    answer = find_subrange(inputs, invalid_number)
    assert answer == 62


def part_two():
    inputs = load_input_file("input.txt")
    invalid_number = compute(inputs, preamble=25)
    answer = find_subrange(inputs, invalid_number)
    print(f"\n# Answer: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
