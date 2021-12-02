import re

from lib.AoC import get_lines


def calc_position():
    lines = get_lines(__file__, 'input.txt')
    horizontal = 0
    depth = 0
    for line in lines:
        direction, amount = re.split('\\s+', line)
        if 'forward' in direction:
            horizontal += int(amount)
        elif 'down' in direction:
            depth += int(amount)
        elif 'up' in direction:
            depth -= int(amount)
    print(f'{horizontal}, {depth}')
    print(f'{horizontal*depth}')


def calc_position_with_aim():
    lines = get_lines(__file__, 'input.txt')
    horizontal = 0
    aim = 0
    depth = 0
    for line in lines:
        direction, amount = re.split('\\s+', line)
        if 'forward' in direction:
            horizontal += int(amount)
            depth += aim * int(amount)
        elif 'down' in direction:
            aim += int(amount)
        elif 'up' in direction:
            aim -= int(amount)
    print(f'{horizontal}, {depth}')
    print(f'{horizontal*depth}')


calc_position()
calc_position_with_aim()
