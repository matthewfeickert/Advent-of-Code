def process_input(input):
    return list(map(int, input.split(",")))


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
3,4,3,1,2\
"""
test_data = process_input(test_string)


def compute_population(inputs, days):
    # spawn rate is 7
    fish = {time: inputs.count(time) for time in range(9)}

    for _ in range(days):
        (
            fish[8],
            fish[7],
            fish[6],
            fish[5],
            fish[4],
            fish[3],
            fish[2],
            fish[1],
            fish[0],
        ) = (
            fish[0],
            fish[8],
            fish[7] + fish[0],
            fish[6],
            fish[5],
            fish[4],
            fish[3],
            fish[2],
            fish[1],
        )
    return sum(fish.values())


def test_part_one():
    assert compute_population(test_data, days=18) == 26
    assert compute_population(test_data, days=80) == 5934


def part_one():
    inputs = load_input_file("input.txt")
    answer = compute_population(inputs, days=80)
    print(f"\n# Answer: {answer}")


def test_part_two():
    assert compute_population(test_data, days=256) == 26984457539


def part_two():
    inputs = load_input_file("input.txt")
    answer = compute_population(inputs, days=256)
    print(f"\n# Answer: {answer}")


if __name__ == "__main__":
    test_part_one()
    part_one()
    test_part_two()
    part_two()
