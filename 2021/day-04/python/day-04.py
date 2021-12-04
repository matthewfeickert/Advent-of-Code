from math import ceil


def process_input(input, card_size=5):
    data = input.splitlines()
    draw_order = list(map(int, data[0].split(",")))
    card_data = [x for x in data[1:] if x != ""]
    cards = [
        card_data[x : x + card_size]  # noqa: E203
        for x in range(0, len(card_data), card_size)
    ]
    cards = [
        [list(map(int, [x for x in row.split(" ") if x != ""])) for row in card]
        for card in cards
    ]

    return draw_order, cards


def load_input_file(path):
    with open(path) as input_file:
        return process_input(input_file.read())


test_string = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7\
"""
test_data = process_input(test_string)


def play_bingo(inputs):
    draw_order, cards = inputs
    card_size = len(cards[0])
    # marker_value = -1

    winning_card = None

    # set free space
    free_space_coordinate = ceil(card_size / 2) - 1
    for card in cards:
        card[free_space_coordinate][free_space_coordinate] = -1

    for draw_number in draw_order:
        for card in cards:
            for row in card:
                if draw_number in row:
                    row[row.index(draw_number)] = -1

        for card in cards:
            if card_size in [row.count(-1) for row in card]:
                winning_card = card
            elif card_size in [
                [row[idx] for row in card].count(-1) for idx in range(card_size)
            ]:
                winning_card = card
            elif [row[idx] for idx, row in enumerate(card)].count(-1) == card_size:
                winning_card = card

            if winning_card is not None:
                card_sum = sum(sum(x for x in row if x > 0) for row in winning_card)
                return card_sum, draw_number


def test_part_one():
    card_sum, draw_number = play_bingo(test_data)
    assert card_sum, draw_number == (188, 24)
    assert card_sum * draw_number == 4512


def part_one():
    inputs = load_input_file("input.txt")
    card_sum, draw_number = play_bingo(inputs)
    print(card_sum, draw_number)
    answer = card_sum * draw_number
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
