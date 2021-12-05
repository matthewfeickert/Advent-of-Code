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


def grid_str(grid):
    grid_size = int(pow(len(grid.values()), 0.5))
    grid_text = ""
    for idx, y in enumerate(range(grid_size)):
        for x in range(grid_size):
            grid_value = grid[(x, y)]
            grid_text += str(grid_value) if grid_value > 0 else "."
        if idx < grid_size - 1:
            grid_text += "\n"
    return grid_text


def compute_grid(inputs, allow_diagonals=False):
    grid_size = max(max(max(y) for y in x) for x in inputs) + 1

    grid = {}
    for y in range(grid_size):
        for x in range(grid_size):
            grid[(x, y)] = 0

    for coord in inputs:
        [x1, y1], [x2, y2] = coord

        if x1 != x2 and y1 != y2 and not allow_diagonals:
            continue
        if x1 == x2:
            y_range = range(y1, y2 + 1) if y2 > y1 else range(y2, y1 + 1)
            line_points = [(x1, y) for y in y_range]
        elif y1 == y2:
            x_range = range(x1, x2 + 1) if x2 > x1 else range(x2, x1 + 1)
            line_points = [(x, y1) for x in x_range]
        else:
            x_range = range(x1, x2 + 1) if x2 > x1 else reversed(range(x2, x1 + 1))
            y_range = range(y1, y2 + 1) if y2 > y1 else reversed(range(y2, y1 + 1))
            line_points = [
                (x, y)
                for x, y in zip(
                    [x for x in x_range],
                    [y for y in y_range],
                )
            ]

        for point in line_points:
            grid[point] += 1

    return grid


def test_part_one():
    grid = compute_grid(test_data, allow_diagonals=False)
    assert (
        grid_str(grid)
        == """\
.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....\
"""
    )
    assert sum(x >= 2 for x in grid.values()) == 5


def part_one():
    inputs = load_input_file("input.txt")
    grid = compute_grid(inputs, allow_diagonals=False)
    answer = sum(x >= 2 for x in grid.values())
    print(f"\n# Answer: {answer}")


def test_part_two():
    grid = compute_grid(test_data, allow_diagonals=True)
    assert (
        grid_str(grid)
        == """\
1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....\
"""
    )
    assert sum(x >= 2 for x in grid.values()) == 12


def part_two():
    inputs = load_input_file("input.txt")
    grid = compute_grid(inputs, allow_diagonals=True)
    answer = sum(x >= 2 for x in grid.values())
    print(f"\n# Answer: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
