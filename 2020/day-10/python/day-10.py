def load_input_file(path):
    with open(path) as input_file:
        return [int(line.strip()) for line in input_file]


def find_chain(inputs, offset):
    ratings = sorted(inputs)
    ground = 0
    joltage_diffs = [ratings[0] - ground]
    joltage_diffs += [j - i for i, j in zip(ratings, ratings[1:])]
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


def count_permutations(inputs, offset):
    ratings = sorted(inputs)
    ratings.append(ratings[-1] + offset)

    step_sizes = [x + 1 for x in range(offset)]
    ways = [1] + [0] * ratings[-1]

    for idx in ratings:
        ways[idx] = sum([ways[idx - step] for step in step_sizes])
    return ways[-1]


def test_part_two():
    inputs = load_input_file("test_data_1.txt")
    ways = count_permutations(inputs, offset=3)
    assert ways == 8

    inputs = load_input_file("test_data_2.txt")
    ways = count_permutations(inputs, offset=3)
    assert ways == 19208


def part_two():
    inputs = load_input_file("input.txt")
    answer = count_permutations(inputs, offset=3)
    print(f"\n# Distinct ways to arrange adapters: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
