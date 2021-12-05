def process_input(input):
    data = [line.split(" -> ") for line in input.splitlines()]
    return [tuple(list(map(int, x.split(","))) for x in pair) for pair in data]


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2\
"""
test_data = process_input(test_string)


def grid_print(grid, grid_size):
    grid_text = ""
    for y in range(grid_size):
        for x in range(grid_size):
            grid_value = grid[(x, y)]
            grid_text += str(grid_value) if grid_value > 0 else "."
        grid_text += "\n"
    print(grid_text)


def count_overlaps(inputs, critical_value=2):
    grid_size = max(max(max(y) for y in x) for x in inputs) + 1

    grid = {}
    for y in range(grid_size):
        for x in range(grid_size):
            grid[(x, y)] = 0

    for coord in inputs:
        [x1, y1], [x2, y2] = coord
        # horizontal lines only
        if x1 != x2 and y1 != y2:
            continue
        if x1 == x2:
            y_range = range(y1, y2 + 1) if y2 > y1 else range(y2, y1 + 1)
            line_points = [(x1, y) for y in y_range]
            for point in line_points:
                grid[point] += 1
        if y1 == y2:
            x_range = range(x1, x2 + 1) if x2 > x1 else range(x2, x1 + 1)
            line_points = [(x, y1) for x in x_range]
            for point in line_points:
                grid[point] += 1

    # grid_print(grid, grid_size)

    return sum(x >= critical_value for x in grid.values())


def test_part_one():
    assert count_overlaps(test_data, critical_value=2) == 5


def part_one():
    inputs = load_input_file("input.txt")
    answer = count_overlaps(inputs, critical_value=2)
    print(f"\n# Answer: {answer}")


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
