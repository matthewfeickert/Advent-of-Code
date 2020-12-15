import re


def load_input_file(path):
    pattern = re.compile(r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)$")  # noqa: W605
    results = []
    with open(path) as input_file:
        for line in input_file:
            if line.startswith("mask"):
                results.append({"mask": line.split("=")[-1].strip(), "instruct": []})
                continue

            matches = pattern.search(line)
            results[-1]["instruct"].append(matches.groupdict())
            # Get ints
            instruction = results[-1]["instruct"][-1]
            for key, value in instruction.items():
                instruction[key] = int(instruction[key])
    return results


def apply_mask(mask, value):
    value = f"{value:b}".zfill(len(mask))
    return int("".join(v if m == "X" else m for m, v in zip(mask, value)), 2)


def execute_program(inputs):
    memory = {}
    for group in inputs:
        mask = group["mask"]
        for instruct in group["instruct"]:
            memory[int(instruct["address"])] = apply_mask(mask, instruct["value"])
    return memory


def test_part_one():
    inputs = load_input_file("test_data.txt")
    memory = execute_program(inputs)
    assert memory == {8: 64, 7: 101}
    assert sum(memory.values()) == 165


def part_one():
    inputs = load_input_file("input.txt")
    memory = execute_program(inputs)
    answer = sum(memory.values())
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
