def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def parse_inputs(inputs):
    timestamp = int(inputs[0])
    bus_ids = [int(id) if id != "x" else -1 for id in inputs[1].split(",")]
    return timestamp, bus_ids


def earliest_time(timestamp, ids):
    ids = [id for id in ids if id != -1]
    quotients = [timestamp // id for id in ids]
    depart_time = [(q * id) + id for q, id in zip(quotients, ids)]
    min_depart_time = min(depart_time)
    min_depart_idx = depart_time.index(min_depart_time)

    earliest_bus_id = ids[min_depart_idx]
    wait_time = depart_time[min_depart_idx] - timestamp
    return earliest_bus_id * wait_time


def find_time(ids):
    # c.f. https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    # use product of solved busses as step
    bus_offsets = sorted((idx, offset) for offset, idx in enumerate(ids) if idx != -1)
    depart, offset = bus_offsets.pop()
    next_time = depart - offset

    for trip_time, wait_time in reversed(bus_offsets):
        while (next_time + wait_time) % trip_time:
            next_time += depart
        depart *= trip_time
    return next_time


def test_part_one():
    inputs = load_input_file("test_data.txt")
    timestamp, bus_ids = parse_inputs(inputs)
    assert earliest_time(timestamp, bus_ids) == 295


def part_one():
    inputs = load_input_file("input.txt")
    timestamp, bus_ids = parse_inputs(inputs)
    answer = earliest_time(timestamp, bus_ids)
    print(f"\n# Part one answer: {answer}")


def test_part_two():
    inputs = load_input_file("test_data.txt")
    timestamp, bus_ids = parse_inputs(inputs)
    assert find_time([17, -1, 13, 19]) == 3417
    assert find_time([67, 7, 59, 61]) == 754018
    assert find_time([67, -1, 7, 59, 61]) == 779210
    assert find_time([67, 7, -1, 59, 61]) == 1261476
    assert find_time([1789, 37, 47, 1889]) == 1202161486


def part_two():
    inputs = load_input_file("input.txt")
    _, bus_ids = parse_inputs(inputs)
    answer = find_time(bus_ids)
    print(f"\n# Part two answer: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
