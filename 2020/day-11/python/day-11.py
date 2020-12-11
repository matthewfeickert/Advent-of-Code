from copy import deepcopy


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def get_adjacent(seat, seats):
    # 1 2 3
    # 4 x 5
    # 6 7 8
    seat_row, seat_idx = seat
    n_rows = len(seats)
    n_seats = len(seats[0])

    seats_adjacent = 8 * [None]
    # top
    if seat_row != 0:
        if seat_idx != 0:
            seats_adjacent[0] = seats[seat_row - 1][seat_idx - 1]
        seats_adjacent[1] = seats[seat_row - 1][seat_idx]
        if seat_idx != n_seats - 1:
            seats_adjacent[2] = seats[seat_row - 1][seat_idx + 1]
    # sides
    if seat_idx != 0:
        seats_adjacent[3] = seats[seat_row][seat_idx - 1]
    if seat_idx != n_seats - 1:
        seats_adjacent[4] = seats[seat_row][seat_idx + 1]
    # bottom
    if seat_row != n_rows - 1:
        if seat_idx != 0:
            seats_adjacent[5] = seats[seat_row + 1][seat_idx - 1]
        seats_adjacent[6] = seats[seat_row + 1][seat_idx]
        if seat_idx != n_seats - 1:
            seats_adjacent[7] = seats[seat_row + 1][seat_idx + 1]

    return seats_adjacent


def apply_rules(data, tolerance=4):
    # Need to apply simultaneously
    new_seats = deepcopy(data)
    for row_idx, row in enumerate(data):
        for seat_idx, seat in enumerate(row):
            # Occupy if empty
            if data[row_idx][seat_idx] == "L":
                if get_adjacent((row_idx, seat_idx), data).count("#") == 0:
                    new_seats[row_idx][seat_idx] = "#"
            # Vacate if too full
            if data[row_idx][seat_idx] == "#":
                if get_adjacent((row_idx, seat_idx), data).count("#") >= tolerance:
                    new_seats[row_idx][seat_idx] = "L"
    return new_seats


def print_seats(seats_a, seats_b):
    print("\nPrevious       New")
    for row_a, row_b in zip(seats_a, seats_b):
        print("".join(row_a), "   ", "".join(row_b))


def converged_seat_map(seats, tolerance):
    seat_history = [deepcopy(seats)]
    converged = False

    new_seats = deepcopy(seats)
    while not converged:
        new_seats = apply_rules(new_seats, tolerance)
        # print_seats(seat_history[-1], new_seats)
        if new_seats == seat_history[-1]:
            converged = True
        else:
            seat_history.append(deepcopy(new_seats))

    return seat_history[-1]


def test_part_one():
    inputs = load_input_file("test_data.txt")
    seats = [list(row) for row in inputs]
    # print(seats)
    assert get_adjacent((1, 1), seats) == ["L", ".", "L", "L", "L", "L", ".", "L"]
    assert get_adjacent((9, 1), seats) == ["L", ".", "L", "L", "L", None, None, None]

    converged_map = converged_seat_map(seats)
    occupied_seats = sum([row.count("#") for row in converged_map])
    assert occupied_seats == 37


def part_one():
    inputs = load_input_file("input.txt")
    seats = [list(row) for row in inputs]

    converged_map = converged_seat_map(seats, tolerance=4)
    occupied_seats = sum([row.count("#") for row in converged_map])
    assert occupied_seats == 2126
    print(f"\n# Answer: {occupied_seats}")


def apply_rules_two(data, tolerance=5):
    # Need to apply simultaneously
    new_seats = deepcopy(data)
    for row_idx, row in enumerate(data):
        for seat_idx, seat in enumerate(row):
            # Occupy if empty
            if data[row_idx][seat_idx] == "L":
                if get_adjacent((row_idx, seat_idx), data).count("#") == 0:
                    new_seats[row_idx][seat_idx] = "#"
            # Vacate if too full
            if data[row_idx][seat_idx] == "#":
                if get_adjacent((row_idx, seat_idx), data).count("#") >= tolerance:
                    new_seats[row_idx][seat_idx] = "L"
    return new_seats


def test_part_two():
    inputs = load_input_file("test_data.txt")
    seats = [list(row) for row in inputs]

    converged_map = converged_seat_map(seats, tolerance=5)
    occupied_seats = sum([row.count("#") for row in converged_map])
    assert occupied_seats == 26


def part_two():
    # inputs = load_input_file("input.txt")
    # print(f"\n# Answer: {answer}")
    pass


if __name__ == "__main__":
    # test_part_one()
    # part_one()
    test_part_two()
    # part_two()
