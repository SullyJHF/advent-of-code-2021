import re

from AoC import get_lines


def create_sheet(coords):
    max_x = max([coord[0] for coord in coords]) + 1
    max_y = max([coord[1] for coord in coords]) + 1
    sheet = [['.' for x in range(max_x)] for y in range(max_y)]
    for x, y in [(x, y) for x in range(max_x) for y in range(max_y)]:
        if [x, y] in coords:
            sheet[y][x] = '#'
    return sheet


def print_sheet(sheet):
    for row in sheet:
        print(''.join(row))


def fold_sheet(coords, axis, index):
    if axis == 'y':
        folded_coords = [coord for coord in coords if coord[1] < index]
    if axis == 'x':
        folded_coords = [coord for coord in coords if coord[0] < index]
    for coord in coords:
        if axis == 'y' and coord[1] >= index:
            folded_coords.append([coord[0], index - (coord[1] - index)])
        elif axis == 'x' and coord[0] >= index:
            folded_coords.append([index - (coord[0] - index), coord[1]])
    return folded_coords


def parts_1_and_2():
    raw_lines = get_lines('./inputs/13.txt')
    coords_str = raw_lines[:raw_lines.index('')]
    coords_str = [coord.split(',') for coord in coords_str]
    coords = []
    for coord in coords_str:
        coords.append([int(c) for c in coord])

    regex = re.compile('fold along (\w)=(\d+)')
    foldstrs = raw_lines[raw_lines.index('') + 1:]
    folds = []
    for foldstr in foldstrs:
        match = regex.match(foldstr)
        folds.append([match.group(1), int(match.group(2))])
    for fold in folds:
        coords = fold_sheet(coords, fold[0], fold[1])
        coord_set = set()
        for coord in coords:
            coord_set.add((coord[0], coord[1]))
        print(len(coord_set))
    print_sheet(create_sheet(coords))


if __name__ == '__main__':
    parts_1_and_2()
