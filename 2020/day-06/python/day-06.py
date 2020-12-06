def load_input_file(path):
    with open(path) as input_file:
        entrys = input_file.read().split("\n\n")
        return [entry.replace("\n", "").rstrip() for entry in entrys]


test_data = """\
abc

a
b
c

ab
ac

a
a
a
a

b\
"""


def get_unique(data):
    return "".join(sorted(list(set(data))))


def test_part_one():
    inputs = load_input_file("test_data.txt")
    sets = [get_unique(input) for input in inputs]
    unique_answers = [len(answers) for answers in sets]
    assert unique_answers == [3, 3, 3, 1, 1]
    assert sum(unique_answers) == 11


def part_one():
    inputs = load_input_file("input.txt")
    sets = [get_unique(input) for input in inputs]
    unique_answers = [len(answers) for answers in sets]
    print(f"\n# Answer: {sum(unique_answers)}")


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
