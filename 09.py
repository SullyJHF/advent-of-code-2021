import re
from typing import Counter

from AoC import get_lines


def get_adj(x, y, cells):
    temp = []
    if x != 0:
        temp += [cells[y][x - 1]]
    if x < len(cells[0]) - 1:
        temp += [cells[y][x + 1]]
    if y != 0:
        temp += [cells[y - 1][x]]
    if y < len(cells) - 1:
        temp += [cells[y + 1][x]]

    return temp


def part_1():
    raw_lines = get_lines('./inputs/09.txt')
    width = len(raw_lines[0])
    height = len(raw_lines)
    height_list = [[int(char) for char in line] for line in raw_lines]
    low_points = []
    for y in range(height):
        for x in range(width):
            adj = get_adj(x, y, height_list)
            if min(adj) > height_list[y][x]:
                low_points += [height_list[y][x]]

    print(sum([i + 1 for i in low_points]))


def part_2():
    raw_lines = get_lines('./inputs/09-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()
