# import re


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


def parse_rules(data):
    rules = {}
    for line in data:
        container, contents = line.rstrip(".").split("contain")
        container = container.rstrip(" bags")
        contents = contents.split(",")
        # Do this with regex later
        contents = [bag.lstrip(" ").rstrip(" bag") for bag in contents]
        contents = [bag.lstrip(" ").rstrip(" bags") for bag in contents]
        bags = [{"number": bag[0], "color": bag[2:]} for bag in contents]
        rules[container] = bags
    # return container, bags
    return rules


def can_hold_color(rules, bag_color):
    count = 0
    for color in rules:
        # print(f"\nbag rule: {color}")
        sub_bags = rules[color]
        for bag in sub_bags:
            # print(f"  sub bag: {bag}")
            if bag["color"] == bag_color:
                count += 1
                # print(f"* {color} contains {bag_color}")
            else:
                # Avoiding regex issue
                _contains = False
                if bag["color"] in rules.keys():
                    sub_sub_bags = rules[bag["color"]]
                    # print(f"   sub sub bags: {sub_sub_bags}")
                    for sub_bag in sub_sub_bags:
                        if sub_bag["color"] == bag_color:
                            # count += int(sub_bag["number"])
                            _contains = True
                            count += 1
                            # print(f"* {color} sub bag contains {bag_color}")
                            break
                if _contains:
                    break
                    # count += 1
                    # print(f"* {color} sub bag contains {bag_color}")
    return count


def test_part_one():
    inputs = load_input_file("test_data.txt")
    # rules = [parse_rules(input) for input in inputs]
    rules = parse_rules(inputs)
    # print(rules)
    # can_hold_color([rules[0]], "shiny gold")
    count = can_hold_color(rules, "shiny gold")
    print(count)
    assert count == 4


def part_one():
    inputs = load_input_file("input.txt")
    rules = parse_rules(inputs)
    count = can_hold_color(rules, "shiny gold")
    print(f"\n# Answer: {count}")


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
