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
    end_idx = len(inputs) - 1
    success = False
    while not success:
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

        if idx == end_idx:
            success = True
    return accumulator, success


def test_part_one():
    inputs = load_input_file("test_data.txt")
    ops_list = parse_inputs(inputs)
    accumulator, success = execute_loop(ops_list)
    assert accumulator == 5


def part_one():
    inputs = load_input_file("input.txt")
    ops_list = parse_inputs(inputs)
    accumulator, success = execute_loop(ops_list)
    print(f"\n# Answer: {accumulator}")


def fix_program(inputs):
    new_inputs = None
    # for idx in range(1, len(inputs)):
    for idx in range(len(inputs) + 1):
        print(idx, inputs[idx])
        if inputs[idx]["op"] not in ["jmp", "nop"]:
            continue

        # test_inputs = inputs.copy()
        test_inputs = [*inputs]
        # test_inputs[idx]["op"] = "nop" if test_inputs[idx]["op"] == "jmp" else "jmp"
        # test_inputs[idx]["op"] = "nop" if test_inputs[idx]["op"] == "jmp" else "nop"
        if test_inputs[idx]["op"] == "jmp":
            test_inputs[idx]["op"] = "nop"
        elif test_inputs[idx]["op"] == "nop":
            test_inputs[idx]["op"] = "jmp"
        _, success = execute_loop(test_inputs)
        if success:
            new_inputs = test_inputs
            return execute_loop(new_inputs)


def test_part_two():
    inputs = load_input_file("test_data.txt")
    ops_list = parse_inputs(inputs)
    print(fix_program(ops_list))
    # print(accumulator)


def part_two():
    # inputs = load_input_file("input.txt")
    # print(f"\n# Answer: {answer}")
    pass


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    # part_two()
    # 1205
