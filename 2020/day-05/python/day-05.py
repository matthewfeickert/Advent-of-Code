def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


test_data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def get_row_column(token):
    row_token = token[:-3]
    col_token = token[-3:]
    # int(x, base=10), so use base=2 for binary
    row = int(row_token.replace("F", "0").replace("B", "1"), base=2)
    col = int(col_token.replace("L", "0").replace("R", "1"), base=2)
    return row, col


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
    print(f"\n# Highest seat ID: {max(seat_ids)}")


def part_two():
    inputs = load_input_file("input.txt")
    rows, columns = zip(*[get_row_column(input) for input in inputs])
    seat_ids = sorted([get_seat_id(row, column) for row, column in zip(rows, columns)])
    full_list = [x for x in range(seat_ids[0], seat_ids[-1] + 1)]
    seat_id = set(full_list) - set(seat_ids)
    print(f"\n# Seat ID: {seat_id.pop()}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    part_two()
