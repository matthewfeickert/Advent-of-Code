def process_input(input):
    return list(map(int, input.split(",")))


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
16,1,2,0,4,2,7,1,2,14\
"""
test_data = process_input(test_string)


def compute_fuel(inputs, position):
    return sum(abs(x - position) for x in inputs)


def fuel_minimum(inputs):
    fuel_cost = [compute_fuel(inputs, position) for position in range(max(inputs))]
    return min(fuel_cost)


def test_part_one():
    assert compute_fuel(test_data, position=2) == 37
    assert compute_fuel(test_data, position=1) == 41
    assert compute_fuel(test_data, position=3) == 39
    assert compute_fuel(test_data, position=10) == 71

    assert fuel_minimum(test_data) == 37


def part_one():
    inputs = load_input_file("input.txt")
    answer = fuel_minimum(inputs)
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
