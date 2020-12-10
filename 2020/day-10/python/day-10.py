def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


def find_chain(inputs, offset):
    adapters = sorted(inputs)
    ground = 0
    joltage_diffs = [adapters[0] - ground]
    joltage_diffs += [j - i for i, j in zip(adapters, adapters[1:])]
    joltage_diffs.append(offset)
    return joltage_diffs


def test_part_one():
    inputs = load_input_file("test_data_1.txt")
    diff_chain = find_chain(inputs, offset=3)
    assert diff_chain == [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    assert diff_chain.count(1) == 7
    assert diff_chain.count(3) == 5

    inputs = load_input_file("test_data_2.txt")
    diff_chain = find_chain(inputs, offset=3)
    assert diff_chain.count(1) == 22
    assert diff_chain.count(3) == 10


def part_one():
    inputs = load_input_file("input.txt")
    diff_chain = find_chain(inputs, offset=3)
    answer = diff_chain.count(1) * diff_chain.count(3)
    print(f"\n# Number of 1-jolt diffs times 3-jolt diffs: {answer}")


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
