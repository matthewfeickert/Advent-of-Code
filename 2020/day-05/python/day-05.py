import math


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


test_data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def get_row_column(token):
    row_range = [0, 127]
    row_token = token[:-3]
    column_range = [0, 7]
    column_token = token[-3:]

    for char in row_token:
        if char == "F":
            # Take lower half
            row_range[1] = row_range[0] + int((row_range[1] - row_range[0]) / 2)
        elif char == "B":
            # Take upper half
            row_range[0] = row_range[0] + int(
                math.ceil((row_range[1] - row_range[0]) / 2)
            )

    for char in column_token:
        if char == "L":
            # Take left half
            column_range[1] = column_range[0] + int(
                (column_range[1] - column_range[0]) / 2
            )
        elif char == "R":
            # Take right half
            column_range[0] = column_range[0] + int(
                math.ceil((column_range[1] - column_range[0]) / 2)
            )

    return row_range[0], column_range[0]


def get_seat_id(row, column, factor=8):
    return row * factor + column


def test_part_one():
    inputs = test_data
    rows, columns = zip(*[get_row_column(input) for input in inputs])
    assert list(rows) == [44, 70, 14, 102]
    assert list(columns) == [5, 7, 7, 4]
    seat_ids = [get_seat_id(row, column) for row, column in zip(rows, columns)]
    assert seat_ids == [357, 567, 119, 820]
    assert max(seat_ids) == 820


def part_one():
    inputs = load_input_file("input.txt")
    rows, columns = zip(*[get_row_column(input) for input in inputs])
    seat_ids = [get_seat_id(row, column) for row, column in zip(rows, columns)]
    print(f"\n# Answer: {max(seat_ids)}")


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
