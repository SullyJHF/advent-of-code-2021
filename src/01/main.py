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


def calc_depth_in_threes():
    lines = get_lines(__file__, 'input.txt')

    total_greater_than_last = 0
    last_line = None

    for i in range(len(lines) - 2):
        line_total = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if not last_line:
            last_line = line_total
            continue
        if int(line_total) > int(last_line):
            total_greater_than_last += 1
        last_line = line_total
    print(total_greater_than_last)


calc_depth()
calc_depth_in_threes()
