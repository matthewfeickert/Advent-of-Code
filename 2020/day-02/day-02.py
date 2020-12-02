#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


def parse_data(data):
    parsed_data = []
    for line in data:
        rule, token = line.split(":")
        key = rule[-1]
        _range = rule[:-1].strip().split("-")
        _min, _max = [int(item) for item in _range]
        token = token.strip()
        parsed_data.append({"key": key, "min": _min, "max": _max, "token": token})
    return parsed_data


def validate_data(data_dict):
    if data_dict["key"] not in data_dict["token"]:
        return False
    return (
        data_dict["min"]
        <= data_dict["token"].count(data_dict["key"])
        <= data_dict["max"]
    )


def test_part_one():
    data = parse_data(test_data.copy())
    validity = [validate_data(entry) for entry in data]
    assert sum(validity) == 2


def part_one():
    inputs = load_input_file("input.txt")
    data = parse_data(inputs)
    validity = [validate_data(entry) for entry in data]
    answer = sum(validity)
    print(f"\n# Number of valid passwords: {answer}")


def revalidate_data(data_dict):
    if data_dict["key"] not in data_dict["token"]:
        return False
    lower_bound = data_dict["min"] - 1
    upper_bound = data_dict["max"] - 1
    key = data_dict["key"]
    token = data_dict["token"]
    return (token[lower_bound] == key) ^ (token[upper_bound] == key)


def test_part_two():
    data = parse_data(test_data.copy())
    validity = [revalidate_data(entry) for entry in data]
    assert sum(validity) == 1


def part_two():
    inputs = load_input_file("input.txt")
    data = parse_data(inputs)
    validity = [revalidate_data(entry) for entry in data]
    answer = sum(validity)
    print(f"\n# Number of valid passwords: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
