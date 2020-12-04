#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        entrys = input_file.read().split("\n\n")
        return [entry.replace("\n", " ") for entry in entrys]


test_data = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in\
"""

# required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def create_passport(inputs):
    passport_keys = [
        [pair.split(":")[0] for pair in input.split(" ")] for input in inputs
    ]
    return passport_keys


def validate_passport(passports, required_keys=required_keys):
    valid_passports = [
        all(keys in passport_keys for keys in required_keys)
        for passport_keys in passports
    ]
    return valid_passports


def test_part_one():
    inputs = load_input_file("test_data.txt")
    passport_keys = create_passport(inputs)
    valid_passports = validate_passport(passport_keys)
    assert valid_passports == [True, False, True, False]
    assert sum(valid_passports) == 2


def part_one():
    inputs = load_input_file("input.txt")
    passport_keys = create_passport(inputs)
    valid_passports = validate_passport(passport_keys)
    print(f"\n# Number of valid passports: {sum(valid_passports)}")


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
