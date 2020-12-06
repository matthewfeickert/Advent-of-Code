def load_input_file(path):
    with open(path) as input_file:
        entrys = input_file.read().split("\n\n")
        return [entry.replace("\n", " ").rstrip() for entry in entrys]


def get_unique(data):
    return "".join(list(set(data)))


def get_all_same(data):
    group_answers = "".join(["".join(line.split("  ")) for line in data]).split(" ")
    answers = [set(answer) for answer in group_answers]
    return answers[0].intersection(*answers[0:])


def test_part_one():
    inputs = load_input_file("test_data.txt")
    sets = [get_unique(input.replace(" ", "")) for input in inputs]
    unique_answers = [len(answers) for answers in sets]
    assert unique_answers == [3, 3, 3, 1, 1]
    assert sum(unique_answers) == 11


def part_one():
    inputs = load_input_file("input.txt")
    sets = [get_unique(input.replace(" ", "")) for input in inputs]
    unique_answers = [len(answers) for answers in sets]
    print(f"\n# Number of unique answers: {sum(unique_answers)}")


def test_part_two():
    inputs = load_input_file("test_data.txt")
    unanimous = [get_all_same(input) for input in inputs]
    n_unanimous = [len(answers) for answers in unanimous]
    assert n_unanimous == [3, 0, 1, 1, 1]
    assert sum(n_unanimous) == 6


def part_two():
    inputs = load_input_file("input.txt")
    unanimous = [get_all_same(input) for input in inputs]
    n_unanimous = [len(answers) for answers in unanimous]
    print(f"\n# Number of unanimous answers: {sum(n_unanimous)}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
