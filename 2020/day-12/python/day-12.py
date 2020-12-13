def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def parse_actions(data):
    return [(action[0], int(action[1:])) for action in data]


def manhattan_distance(position):
    return int(sum([abs(position.real), abs(position.imag)]))


def update(coord, action, value, step=0 + 0j):
    if action == "F":
        return coord + value * step
    elif action == "N":
        return coord + value * 1j
    elif action == "S":
        return coord + value * -1j
    elif action == "E":
        return coord + value * 1
    elif action == "W":
        return coord + value * -1
    elif action == "L":
        return coord * ((1j) ** (value // 90))
    elif action == "R":
        return coord * ((-1j) ** (value // 90))


def move(position, direction, actions):
    for action, value in actions:
        if action in "FNSEW":
            position = update(position, action, value, step=direction)
        elif action in "LR":
            direction = update(direction, action, value)
    return position


def test_part_one():
    inputs = load_input_file("test_data.txt")
    actions = parse_actions(inputs)

    position = 0 + 0j  # Origin
    direction = 1 + 0j  # Face east
    position = move(position, direction, actions)
    answer = manhattan_distance(position)
    assert answer == 25


def part_one():
    inputs = load_input_file("input.txt")
    actions = parse_actions(inputs)

    position = 0 + 0j  # Origin
    direction = 1 + 0j  # Face east
    position = move(position, direction, actions)
    answer = manhattan_distance(position)
    print(f"\n# Manhattan distance: {answer}")


def move_waypoint(position, waypoint, actions):
    for action, value in actions:
        if action in "F":
            position = update(position, action, value, step=waypoint)
        elif action in "NSEWLR":
            waypoint = update(waypoint, action, value)
    return position


def test_part_two():
    inputs = load_input_file("test_data.txt")
    actions = parse_actions(inputs)

    position = 0 + 0j  # Origin
    waypoint = 10 + 1j
    position = move_waypoint(position, waypoint, actions)
    answer = manhattan_distance(position)
    assert answer == 286


def part_two():
    inputs = load_input_file("input.txt")
    actions = parse_actions(inputs)

    position = 0 + 0j  # Origin
    waypoint = 10 + 1j
    position = move_waypoint(position, waypoint, actions)
    answer = manhattan_distance(position)
    print(f"\n# Manhattan distance: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
