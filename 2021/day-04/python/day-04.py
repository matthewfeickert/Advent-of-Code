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
    draw_order, boards = inputs
    board_size = len(boards[0])
    # marker_value = -1

    winning_board = None

    # NO FREE SPACE
    # # set free space
    # free_space_coordinate = ceil(board_size / 2) - 1
    # for board in boards:
    #     board[free_space_coordinate][free_space_coordinate] = -1

    for draw_number in draw_order:
        for board in boards:
            for row in board:
                if draw_number in row:
                    row[row.index(draw_number)] = -1

        for board in boards:
            if board_size in [row.count(-1) for row in board]:
                winning_board = board
            elif board_size in [
                [row[idx] for row in board].count(-1) for idx in range(board_size)
            ]:
                winning_board = board
            # DIAGONALS DON'T COUNT
            # elif [row[idx] for idx, row in enumerate(board)].count(-1) == board_size:
            #     winning_board = board

            if winning_board is not None:
                board_sum = sum(sum(x for x in row if x > 0) for row in winning_board)
                return board_sum, draw_number


def test_part_one():
    board_sum, draw_number = play_bingo(test_data)
    assert board_sum, draw_number == (188, 24)
    assert board_sum * draw_number == 4512


def part_one():
    inputs = load_input_file("input.txt")
    board_sum, draw_number = play_bingo(inputs)
    print(board_sum, draw_number)
    answer = board_sum * draw_number
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
