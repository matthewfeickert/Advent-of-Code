def load_input_file(path):
    with open(path) as input_file:
        entrys = input_file.read().split("\n\n")
        return [entry.replace("\n", " ").rstrip() for entry in entrys]


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
    return "".join(list(set(data)))


def get_all_same(data):
    answers = "".join(["".join(line.split("  ")) for line in data]).split(" ")
    individual_answers = [set(answer) for answer in answers]
    # print(individual_answers)
    # if len(individual_answers) > 1:
    return individual_answers[0].intersection(*individual_answers[0:])


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
    print(f"\n# Answer: {sum(unique_answers)}")


def test_part_two():
    inputs = load_input_file("test_data.txt")
    unique_answers = [get_all_same(input) for input in inputs]
    size_intersetcion = [len(interset) for interset in unique_answers]
    assert size_intersetcion == [3, 0, 1, 1, 1]
    assert sum(size_intersetcion) == 6


def part_two():
    inputs = load_input_file("input.txt")
    unique_answers = [get_all_same(input) for input in inputs]
    size_intersetcion = [len(interset) for interset in unique_answers]
    print(f"\n# Answer: {sum(size_intersetcion)}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
