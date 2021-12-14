from AoC import get_lines


def get_adj(x_coord, y_coord, cells):
    temp = []
    for x, y in [(x_coord + i, y_coord + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
        if x < len(cells[0]) and y < len(cells) and x >= 0 and y >= 0:
            temp.append((x, y))
    return temp


def get_flashed(octos):
    temp = []
    for x, y in [(x, y) for x in range(len(octos[0])) for y in range(len(octos))]:
        if octos[x][y] > 9:
            temp.append((x, y))
    return temp


def print_octos(octos):
    for line in octos:
        print(''.join([str(char) for char in line]))


def part_1():
    raw_lines = get_lines('./inputs/11.txt')
    octos = []
    for line in raw_lines:
        octos.append([int(char) for char in line])
    print_octos(octos)
    print()
    flash_count = 0
    steps = 100
    for step in range(steps):
        for x, y in [(x, y) for x in range(len(octos[0])) for y in range(len(octos))]:
            octos[x][y] += 1
        flashed = get_flashed(octos)
        all_flashed = flashed

        while len(flashed):
            for x, y in flashed:
                octos[x][y] = 0
                for xx, yy in get_adj(x, y, octos):
                    if (xx, yy) not in all_flashed:
                        octos[xx][yy] += 1
            flashed = get_flashed(octos)
            all_flashed += flashed
        flash_count += len(all_flashed)
    print(flash_count)


def part_2():
    raw_lines = get_lines('./inputs/11-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()
