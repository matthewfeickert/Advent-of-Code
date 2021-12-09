def process_input(input):
    return [list(map(int, list(x))) for x in input.splitlines()]


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
2199943210
3987894921
9856789892
8767896789
9899965678\
"""
test_data = process_input(test_string)


def risk_level(inputs):
    n_rows = len(inputs)
    n_columns = len(inputs[0])
    low_points = []

    for row_idx, row in enumerate(inputs):
        for idx, number in enumerate(row):
            if idx > 0 and row[idx - 1] <= number:
                continue
            if idx < n_columns - 1 and row[idx + 1] <= number:
                continue
            if row_idx > 0 and inputs[row_idx - 1][idx] <= number:
                continue
            if row_idx < n_rows - 1 and inputs[row_idx + 1][idx] <= number:
                continue
            low_points.append(number)

    risk_penalty = 1
    return sum(height + risk_penalty for height in low_points)


def test_part_one():
    assert risk_level(test_data) == 15


def part_one():
    inputs = load_input_file("input.txt")
    answer = risk_level(inputs)
    print(f"\n# Answer: {answer}")


def get_basins(inputs):
    n_rows = len(inputs)
    n_columns = len(inputs[0])
    basins = []

    nine_index_map = []

    for row_idx, row in enumerate(inputs):
        for idx, number in enumerate(row):
            if number == 9:
                nine_index_map.append([row_idx, idx])

    n_positions = len(nine_index_map)
    basin = []
    used_positions = []
    for idx, position in enumerate(nine_index_map):
        # get horizontal distance to next 9
        if idx < n_positions and position not in used_positions:
            if position[0] == nine_index_map[idx + 1][0]:
                row_idx = position[0]
                # check if there is any area to fill
                if nine_index_map[idx + 1][1] - position[1] > 1:
                    this_idx = position[1]
                    next_idx = nine_index_map[idx + 1][1]
                    basin += inputs[row_idx][this_idx + 1 : next_idx]
                    used_positions.append(position)
                    used_positions.append(nine_index_map[idx + 1])
                    print("Another 9 on same row")
                    print(position, nine_index_map[idx + 1])
                    breakpoint()


def test_part_two():
    assert get_basins(test_data) == 1134


def part_two():
    # inputs = load_input_file("input.txt")
    # print(f"\n# Answer: {answer}")
    pass


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    # part_two()
