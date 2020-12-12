import re


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def parse_actions(data):
    actions = []
    for action in data:
        split_char = re.search("[A-Z]+", action).group(0)
        actions.append([split_char, int(action.split(split_char)[-1])])
    return actions


def test_part_one():
    inputs = load_input_file("test_data.txt")
    actions = parse_actions(inputs)
    facing = "E"
    coords = (0, 0)

    assert execute_action(["L", 180], ("E", (0, 0))) == execute_action(
        ["R", 180], ("E", (0, 0))
    )
    recorded_positions = []
    for action in actions:
        facing, coords = execute_action(action, (facing, coords))
        recorded_positions.append([facing, coords])
    assert recorded_positions == [
        ["E", (10, 0)],
        ["E", (10, 3)],
        ["E", (17, 3)],
        ["S", (17, 3)],
        ["S", (17, -8)],
    ]
    answer = sum([abs(x) for x in coords])
    assert answer == 25


def execute_action(action, state):
    facing, (long, lat) = state
    direction, distance = action
    cardinal_directions = ["N", "E", "S", "W"]

    if direction == "N":
        lat += distance
    if direction == "S":
        lat -= distance
    if direction == "E":
        long += distance
    if direction == "W":
        long -= distance
    if direction in ["L", "R"]:
        rotation = int(distance / 90)
        if direction == "L":
            new_idx = (cardinal_directions.index(facing) - rotation) % len(
                cardinal_directions
            )
        else:
            new_idx = (cardinal_directions.index(facing) + rotation) % len(
                cardinal_directions
            )
        facing = cardinal_directions[new_idx]
    if direction == "F":
        if facing == "N":
            lat += distance
        elif facing == "S":
            lat -= distance
        elif facing == "E":
            long += distance
        elif facing == "W":
            long -= distance

    return facing, (long, lat)


def part_one():
    inputs = load_input_file("input.txt")
    actions = parse_actions(inputs)
    facing = "E"
    coords = (0, 0)

    for action in actions:
        facing, coords = execute_action(action, (facing, coords))
    answer = sum([abs(x) for x in coords])
    print(f"\n# Manhattan distance: {answer}")


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
