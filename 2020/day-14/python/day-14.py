def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def test_part_one():
    inputs = load_input_file("test_data.txt")
    print(inputs)
    # print(f"\n# Answer: {answer}")


def part_one():
    # inputs = load_input_file("input.txt")
    # print(f"\n# Answer: {answer}")
    pass


def test_part_two():
    pass


def part_two():
    # inputs = load_input_file("input.txt")
    # print(f"\n# Answer: {answer}")
    pass


if __name__ == "__main__":
    test_part_one()
    # part_one()
    # test_part_two()
    # part_two()
