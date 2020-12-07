import re


def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


test_data = """\n
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def parse_inputs(data):
    pattern = re.compile(
        r"^(?P<outer_bag>.*?) bags? contain (?P<empty>no other bags)?\s?(?P<inner_bags>.*?)?\.$"  # noqa
    )
    bags_split = re.compile(
        r"(?P<quantity>\d)?\s?(?P<color>[a-zA-Z\s]+?) bags?"
    )  # noqa
    inputs = []
    for line in data:
        match = pattern.match(line)
        inputs.append(match.groupdict())
        inputs[-1]["inner_bags"] = list(
            map(
                # lambda x: x.groupdict() if x else x,
                lambda x: x.groupdict(),
                bags_split.finditer(inputs[-1]["inner_bags"]),
            )
        )
    return inputs


def make_rules(data):
    rules = {}
    for line in data:
        rules[line["outer_bag"]] = {
            "empty": line["empty"] is not None,
            "inner_bags": {},
        }
        outer_bag = rules[line["outer_bag"]]
        for inner_bag in line["inner_bags"]:
            outer_bag["inner_bags"][inner_bag["color"]] = int(inner_bag["quantity"])
    return rules


def can_hold(bag, outer_bag, rules):
    if rules[outer_bag]["empty"]:
        return False
    if bag in rules[outer_bag]["inner_bags"]:
        return True
    for inner_bag in rules[outer_bag]["inner_bags"].keys():
        if can_hold(bag, inner_bag, rules):
            return True
    return False


def count_outer_bag(bag, rules):
    return sum([can_hold(bag, outer_bag, rules) for outer_bag in rules.keys()])


def count_inner_bags(outer_bag, rules):
    total = 0
    if rules[outer_bag]["empty"]:
        return total
    for inner_bag, quantity in rules[outer_bag]["inner_bags"].items():
        total += quantity
        total += quantity * count_inner_bags(inner_bag, rules)
    return total


def test_part_one():
    inputs = load_input_file("test_data.txt")
    parsed_inputs = parse_inputs(inputs)
    rules = make_rules(parsed_inputs)

    assert rules["light red"] == {
        "empty": False,
        "inner_bags": {"bright white": 1, "muted yellow": 2},
    }
    assert rules["dark orange"] == {
        "empty": False,
        "inner_bags": {"bright white": 3, "muted yellow": 4},
    }
    assert rules["bright white"] == {
        "empty": False,
        "inner_bags": {"shiny gold": 1},
    }
    assert rules["muted yellow"] == {
        "empty": False,
        "inner_bags": {"shiny gold": 2, "faded blue": 9},
    }
    assert rules["shiny gold"] == {
        "empty": False,
        "inner_bags": {"dark olive": 1, "vibrant plum": 2},
    }
    assert rules["dark olive"] == {
        "empty": False,
        "inner_bags": {"faded blue": 3, "dotted black": 4},
    }
    assert rules["vibrant plum"] == {
        "empty": False,
        "inner_bags": {"faded blue": 5, "dotted black": 6},
    }

    assert can_hold("shiny gold", "light red", rules)
    assert can_hold("shiny gold", "dark orange", rules)
    assert can_hold("shiny gold", "bright white", rules)
    assert can_hold("shiny gold", "muted yellow", rules)
    assert not can_hold("shiny gold", "shiny gold", rules)
    assert not can_hold("shiny gold", "dark olive", rules)
    assert not can_hold("shiny gold", "vibrant plum", rules)
    assert not can_hold("shiny gold", "faded blue", rules)
    assert not can_hold("shiny gold", "dotted black", rules)

    assert count_outer_bag("shiny gold", rules) == 4


def part_one():
    inputs = load_input_file("input.txt")
    parsed_inputs = parse_inputs(inputs)
    rules = make_rules(parsed_inputs)
    count = count_outer_bag("shiny gold", rules)
    print(f"\n# Answer: {count}")


def test_part_two():
    inputs = load_input_file("test_data.txt")
    parsed_inputs = parse_inputs(inputs)
    rules = make_rules(parsed_inputs)
    count = count_inner_bags("shiny gold", rules)
    assert count == 32


def part_two():
    inputs = load_input_file("input.txt")
    parsed_inputs = parse_inputs(inputs)
    rules = make_rules(parsed_inputs)
    count = count_inner_bags("shiny gold", rules)
    print(f"\n# Answer: {count}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
