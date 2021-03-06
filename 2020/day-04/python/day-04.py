#!/usr/bin/env python3


def load_input_file(path):
    with open(path) as input_file:
        entrys = input_file.read().split("\n\n")
        return [entry.replace("\n", " ").rstrip() for entry in entrys]


required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def create_passport(inputs):
    passports = []
    for input in inputs:
        passport = {}
        for entry in input.split(" "):
            key, value = entry.split(":")
            passport[key] = value
        passports.append(passport)
    return passports


def validate_passport(passports, required_keys=required_keys):
    valid_passports = [
        all(keys in passport.keys() for keys in required_keys) for passport in passports
    ]
    return valid_passports


def validate_keys(passports):
    valid_passports = []
    for port in passports:
        if int(port["byr"]) < 1920 or int(port["byr"]) > 2002:
            continue
        if int(port["iyr"]) < 2010 or int(port["iyr"]) > 2020:
            continue
        if int(port["eyr"]) < 2020 or int(port["eyr"]) > 2030:
            continue
        if port["hgt"][-2:] not in ["cm", "in"]:
            continue
        if port["hgt"][-2:] == "cm":
            height = int(port["hgt"][:-2])
            if height < 150 or height > 193:
                continue
        if port["hgt"][-2:] == "in":
            height = int(port["hgt"][:-2])
            if height < 59 or height > 76:
                continue
        hair_color = port["hcl"]
        if len(hair_color) != 7:
            continue
        else:
            if hair_color[0] != "#":
                continue
        if port["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        if len(port["pid"]) != 9:
            continue
        if not port["pid"].isdecimal():
            continue
        valid_passports.append(port)
    return valid_passports


def test_part_one():
    inputs = load_input_file("test_data.txt")
    passports = create_passport(inputs)
    valid_passports = validate_passport(passports)
    assert valid_passports == [True, False, True, False]
    assert sum(valid_passports) == 2


def part_one():
    inputs = load_input_file("input.txt")
    passports = create_passport(inputs)
    valid_passports = validate_passport(passports)
    print(f"\n# Number of valid passports: {sum(valid_passports)}")


def test_part_two():
    inputs = load_input_file("test_invalid.txt")
    passports = create_passport(inputs)
    valid_passports = [
        x for idx, x in enumerate(passports) if validate_passport(passports)[idx]
    ]
    valid_passports = validate_keys(valid_passports)
    assert len(valid_passports) == 0

    inputs = load_input_file("test_valid.txt")
    passports = create_passport(inputs)
    valid_passports = [
        x for idx, x in enumerate(passports) if validate_passport(passports)[idx]
    ]
    valid_passports = validate_keys(valid_passports)
    assert len(valid_passports) == 4


def part_two():
    inputs = load_input_file("input.txt")
    passports = create_passport(inputs)
    valid_passports = [
        x for idx, x in enumerate(passports) if validate_passport(passports)[idx]
    ]
    valid_passports = validate_keys(valid_passports)
    print(f"\n# Number of valid passports: {len(valid_passports)}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
