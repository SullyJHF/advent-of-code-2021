import re

from AoC import get_lines


def get_submarine_lines(raw_lines):
    array_lines = [re.compile('\s+->\s+').split(line.strip()) for line in raw_lines]
    lines = []
    for array_line in array_lines:
        line = {
            'x1': int(array_line[0].split(',')[0]),
            'y1': int(array_line[0].split(',')[1]),
            'x2': int(array_line[1].split(',')[0]),
            'y2': int(array_line[1].split(',')[1])
        }
        line['straight'] = line['x1'] == line['x2'] or line['y1'] == line['y2']
        lines.append(line)
    return lines


def make_grid(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if line['x1'] > max_x:
            max_x = line['x1']
        if line['x2'] > max_x:
            max_x = line['x2']
        if line['y1'] > max_y:
            max_y = line['y1']
        if line['y2'] > max_y:
            max_y = line['y2']

    return [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]


def get_all_line_points(line):
    width = abs(line['x2'] - line['x1'])
    height = abs(line['y2'] - line['y1'])
    points = [{
        'x': line['x1'],
        'y': line['y1'],
    }, {
        'x': line['x2'],
        'y': line['y2'],
    }]
    if width == 0 or height == 0:
        for x in range(1, width):
            min_x = min(line['x1'], line['x2'])
            points.append({
                'x': x + min_x,
                'y': 0 + line['y2']
            })
        for y in range(1, height):
            min_y = min(line['y1'], line['y2'])
            points.append({
                'x': 0 + line['x2'],
                'y': y + min_y
            })
    else:
        # diagonal line
        for i in range(1, width):
            m = (line['y2'] - line['y1']) / (line['x2'] - line['x1'])
            c = line['y1'] - line['x1'] * m
            # min_x = min(line['x1'], line['x2'])
            x = int(i + min(line['x2'], line['x1']))
            y = int(m * x + c)
            points.append({
                'x': x,
                'y': y
            })
    return points


def fill_grid(grid, line):
    points = get_all_line_points(line)
    for point in points:
        grid[point['y']][point['x']] += 1


def print_grid(grid):
    for grid_line in grid:
        print(grid_line)


def calc_grid(grid):
    total = 0
    for line in grid:
        for cell in line:
            if cell >= 2:
                total += 1
    return total


def part_1():
    raw_lines = get_lines('./inputs/05.txt')
    lines = get_submarine_lines(raw_lines)
    grid = make_grid(lines)
    for line in lines:
        if not line['straight']:
            continue
        fill_grid(grid, line)
    print_grid(grid)
    total = calc_grid(grid)
    print(total)


def part_2():
    raw_lines = get_lines('./inputs/05.txt')
    lines = get_submarine_lines(raw_lines)
    grid = make_grid(lines)
    for line in lines:
        fill_grid(grid, line)
    print_grid(grid)
    total = calc_grid(grid)
    print(total)


if __name__ == '__main__':
    # part_1()
    part_2()
