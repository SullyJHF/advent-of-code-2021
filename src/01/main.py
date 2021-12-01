from lib.AoC import get_lines


def calc_depth():
    lines = get_lines(__file__, 'input.txt')

    total_greater_than_last = 0
    last_line = None

    for line in lines:
        if not last_line:
            last_line = line
            continue
        if int(line) > int(last_line):
            total_greater_than_last += 1
        last_line = line
    print(total_greater_than_last)


calc_depth()
