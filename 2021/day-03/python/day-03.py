def process_input(input):
    return input.splitlines()


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010\
"""
test_data = process_input(test_string)


def calculate_rates_in_decimal(inputs):
    epsilon = None
    delta = None
    bits = []
    for index in range(len(inputs[0])):
        print(index)
        column = [x[index] for x in inputs]
        bits.append(max(column, key=column.count))
    epsilon = int("".join(bits), base=2)
    delta_bits = "".join([str(1 - int(x)) for x in bits])
    delta = int("".join(delta_bits), base=2)

    return epsilon, delta


def test_part_one():
    epsilon, delta = calculate_rates_in_decimal(test_data)
    assert epsilon, delta == (22, 9)
    assert epsilon * delta == 198


def part_one():
    inputs = load_input_file("input.txt")
    epsilon, delta = calculate_rates_in_decimal(inputs)
    answer = epsilon * delta
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