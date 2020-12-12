import re


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def parse_actions(data):
    actions = []
    for action in data:
        split_char = re.search("[A-Z]+", action).group(0)
        actions.append([split_char, action.split(split_char)[-1]])
    return actions


def test_part_one():
    inputs = load_input_file("test_data.txt")
    actions = parse_actions(inputs)
    print(actions)


def execute_action(action, coords):
    long, lat = coords
    direction, distance = action


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
