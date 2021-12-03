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

    gamma_rate = int(gamma_rate, base=2)
    epsilon_rate = int(epsilon_rate, base=2)

    return gamma_rate, epsilon_rate


def test_part_one():
    gamma, epsilon = get_rates(test_data)
    assert gamma, epsilon == (22, 9)
    assert gamma * epsilon == 198


def part_one():
    inputs = load_input_file("input.txt")
    gamma, epsilon = get_rates(inputs)
    answer = gamma * epsilon
    print(f"\n# Power consumption: {answer}")


def oxygen_generation(inputs):
    numbers = inputs.copy()
    for index in range(len(numbers[0])):
        column = [x[index] for x in numbers]

        bit_key = "1" if column.count("1") >= column.count("0") else "0"

        remove_list = [number for number in numbers if number[index] != bit_key]
        for number in remove_list:
            numbers.remove(number)
        if len(numbers) == 1:
            break

    return int(numbers[0], base=2)


def co2_scrubber(inputs):
    numbers = inputs.copy()
    for index in range(len(numbers[0])):
        column = [x[index] for x in numbers]

        bit_key = "1" if column.count("1") < column.count("0") else "0"

        remove_list = [number for number in numbers if number[index] != bit_key]
        for number in remove_list:
            numbers.remove(number)
        if len(numbers) == 1:
            break

    return int(numbers[0], base=2)


def test_part_two():
    oxygen_rating = oxygen_generation(test_data)
    co2_rating = co2_scrubber(test_data)
    assert oxygen_rating, co2_rating == (23, 10)
    assert oxygen_rating * co2_rating == 230


def part_two():
    inputs = load_input_file("input.txt")
    oxygen_rating = oxygen_generation(inputs)
    co2_rating = co2_scrubber(inputs)
    answer = oxygen_rating * co2_rating
    print(f"\n# Answer: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
