from itertools import permutations


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
