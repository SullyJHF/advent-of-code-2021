import re

from AoC import get_lines


def get_boards(lines):
    boards = []
    board_index = -1
    board_size = 0
    index = 0
    line = lines[index]
    for line in lines:
        if not line:
            board_index += 1
            boards.insert(board_index, [])
            continue
        cells = re.compile('\s+').split(line.strip())
        board_size = len(cells)
        boards[board_index] += cells

    return boards, board_size


def calc_win(numbers, board, board_size):
    # print(numbers)
    marked_board = board
    marked_board = [True if number in numbers else False for number in board]
    for i in range(board_size):
        row_index = i * board_size
        row = marked_board[row_index: row_index + board_size]
        # print(row)
        if all(row):
            return marked_board

        col = []
        for j in range(board_size):
            col.append(marked_board[i + j * board_size])
        # print(col)
        if all(col):
            return board
    return False


def part_1():
    raw_lines = get_lines('./inputs/04.txt')
    draw_numbers = raw_lines[0].split(',')
    boards, board_size = get_boards(raw_lines[1:])

    current_draws = []
    marked_board = None
    winning_board = None
    for draw in draw_numbers:
        current_draws.append(draw)
        for board in boards:
            marked_board = calc_win(current_draws, board, board_size)
            # print(marked_board)
            if marked_board:
                winning_board = board
                break
        if marked_board:
            break
    print(current_draws)
    print(winning_board)
    total = 0
    for num in winning_board:
        if num not in current_draws:
            total += int(num)
    print(total * int(current_draws[-1]))


def part_2():
    raw_lines = get_lines('./inputs/04-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()
