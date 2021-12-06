def process_input(input):
    return list(map(int, input.split(",")))


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
3,4,3,1,2\
"""
test_data = process_input(test_string)


def model_population(inputs, days):
    spawn_rate = 7
    population = inputs.copy()
    # print(f"population on day 0: {population}")
    for _ in range(days):
        new_fish = []
        day_population = []
        for fish in population:
            if fish > 0:
                day_population.append(fish - 1)
            if fish == 0:
                day_population.append(spawn_rate - 1)
                new_fish.append(spawn_rate + 1)
        # day is over, add new fish so don't count them
        population = day_population + new_fish

    # print(f"population on day {days}: {population}")
    return population


def test_part_one():
    assert model_population(test_data, days=1) == [2, 3, 2, 0, 1]
    assert model_population(test_data, days=2) == [1, 2, 1, 6, 0, 8]
    assert model_population(test_data, days=3) == [0, 1, 0, 5, 6, 7, 8]
    assert model_population(test_data, days=4) == [6, 0, 6, 4, 5, 6, 7, 8, 8]
    assert model_population(test_data, days=5) == [5, 6, 5, 3, 4, 5, 6, 7, 7, 8]
    assert model_population(test_data, days=6) == [4, 5, 4, 2, 3, 4, 5, 6, 6, 7]
    assert model_population(test_data, days=7) == [3, 4, 3, 1, 2, 3, 4, 5, 5, 6]
    assert model_population(test_data, days=8) == [2, 3, 2, 0, 1, 2, 3, 4, 4, 5]
    assert model_population(test_data, days=9) == [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 8]
    assert model_population(test_data, days=10) == [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8]
    assert model_population(test_data, days=11) == [
        6,
        0,
        6,
        4,
        5,
        6,
        0,
        1,
        1,
        2,
        6,
        7,
        8,
        8,
        8,
    ]
    assert model_population(test_data, days=12) == [
        5,
        6,
        5,
        3,
        4,
        5,
        6,
        0,
        0,
        1,
        5,
        6,
        7,
        7,
        7,
        8,
        8,
    ]
    assert model_population(test_data, days=13) == [
        4,
        5,
        4,
        2,
        3,
        4,
        5,
        6,
        6,
        0,
        4,
        5,
        6,
        6,
        6,
        7,
        7,
        8,
        8,
    ]
    assert model_population(test_data, days=14) == [
        3,
        4,
        3,
        1,
        2,
        3,
        4,
        5,
        5,
        6,
        3,
        4,
        5,
        5,
        5,
        6,
        6,
        7,
        7,
        8,
    ]
    assert model_population(test_data, days=15) == [
        2,
        3,
        2,
        0,
        1,
        2,
        3,
        4,
        4,
        5,
        2,
        3,
        4,
        4,
        4,
        5,
        5,
        6,
        6,
        7,
    ]
    assert model_population(test_data, days=16) == [
        1,
        2,
        1,
        6,
        0,
        1,
        2,
        3,
        3,
        4,
        1,
        2,
        3,
        3,
        3,
        4,
        4,
        5,
        5,
        6,
        8,
    ]
    assert model_population(test_data, days=17) == [
        0,
        1,
        0,
        5,
        6,
        0,
        1,
        2,
        2,
        3,
        0,
        1,
        2,
        2,
        2,
        3,
        3,
        4,
        4,
        5,
        7,
        8,
    ]
    assert model_population(test_data, days=18) == [
        6,
        0,
        6,
        4,
        5,
        6,
        0,
        1,
        1,
        2,
        6,
        0,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        6,
        7,
        8,
        8,
        8,
        8,
    ]

    assert len(model_population(test_data, days=18)) == 26
    assert len(model_population(test_data, days=80)) == 5934


def part_one():
    inputs = load_input_file("input.txt")
    answer = len(model_population(inputs, days=80))
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
