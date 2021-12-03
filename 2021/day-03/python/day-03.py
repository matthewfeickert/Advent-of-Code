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


def get_rates(inputs):
    gamma_rate = ""
    epsilon_rate = ""

    for column in zip(*inputs):
        ones_count = column.count("1")
        zero_count = len(column) - ones_count

        gamma_rate += "1" if ones_count >= zero_count else "0"
        epsilon_rate += "0" if ones_count >= zero_count else "1"

    return gamma_rate, epsilon_rate


def test_part_one():
    gamma, epsilon = list(map(lambda x: int(x, base=2), get_rates(test_data)))
    assert gamma, epsilon == (22, 9)
    assert gamma * epsilon == 198


def part_one():
    inputs = load_input_file("input.txt")
    gamma, epsilon = list(map(lambda x: int(x, base=2), get_rates(inputs)))
    answer = gamma * epsilon
    print(f"\n# Power consumption: {answer}")


def gas_rates(inputs, gas):
    numbers = inputs.copy()

    rate_type = 0 if gas == "oxygen" else 1

    idx = 0
    while len(numbers) > 1:
        bit_key = get_rates(numbers)[rate_type][idx]
        numbers = [number for number in numbers if number[idx] == bit_key]
        idx += 1

    return int(numbers[0], base=2)


def test_part_two():
    oxygen_rating = gas_rates(test_data, "oxygen")
    co2_rating = gas_rates(test_data, "co2")
    assert oxygen_rating, co2_rating == (23, 10)
    assert oxygen_rating * co2_rating == 230


def part_two():
    inputs = load_input_file("input.txt")
    oxygen_rating = gas_rates(inputs, "oxygen")
    co2_rating = gas_rates(inputs, "co2")
    answer = oxygen_rating * co2_rating
    print(f"\n# Life support rating: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
