def process_input(input):
    return [[y.split(" ") for y in x.split(" | ")] for x in input.splitlines()]


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


# unique signal patterns | four digit output value
test_string = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce\
"""
test_data = process_input(test_string)


def count_unique(inputs):
    info_map = {n: 0 for n in range(10)}

    for signals, outputs in inputs:
        signal_length = list(map(len, signals))
        output_length = list(map(len, outputs))

        unique_numbers = {1: 2, 4: 4, 7: 3, 8: 7}

        for key, value in unique_numbers.items():
            if value in signal_length and value in output_length:
                info_map[key] += output_length.count(value)

    return sum(info_map.values())


def test_part_one():
    assert count_unique(test_data) == 26


def part_one():
    inputs = load_input_file("input.txt")
    answer = count_unique(inputs)
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
