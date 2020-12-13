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
