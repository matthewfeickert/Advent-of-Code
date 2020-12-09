def load_input_file(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


test_data = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def parse_inputs(inputs):
    output = []
    for x in inputs:
        op, acc_value = x.split()
        output.append({"op": op, "offset": int(acc_value)})
    return output


def execute_loop(inputs):
    accumulator = 0
    visited_idx = []
    idx = 0
    while True:
        if inputs[idx]["op"] == "acc":
            if idx in visited_idx:
                break
            visited_idx.append(idx)
            accumulator += inputs[idx]["offset"]
            idx += 1
        if inputs[idx]["op"] == "jmp":
            if idx in visited_idx:
                break
            visited_idx.append(idx)
            idx += inputs[idx]["offset"]
        if inputs[idx]["op"] == "nop":
            if idx in visited_idx:
                break
            visited_idx.append(idx)
            idx += 1
    return accumulator


def test_part_one():
    inputs = load_input_file("test_data.txt")
    ops_list = parse_inputs(inputs)
    accumulator = execute_loop(ops_list)
    assert accumulator == 5


def part_one():
    inputs = load_input_file("input.txt")
    ops_list = parse_inputs(inputs)
    accumulator = execute_loop(ops_list)
    print(f"\n# Answer: {accumulator}")


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
