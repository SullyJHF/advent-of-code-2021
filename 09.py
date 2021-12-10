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


def get_adj_coords(x, y, cells):
    temp = []
    if x != 0:
        temp.append([x - 1, y])
    if x < len(cells[0]) - 1:
        temp.append([x + 1, y])
    if y != 0:
        temp.append([x, y - 1])
    if y < len(cells) - 1:
        temp.append([x, y + 1])

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


def find_basin(x, y, cells, seen):
    basin_arr = [(x, y)]
    adj = get_adj_coords(x, y, cells)
    adj_no_nines = [[x, y] for x, y in adj if cells[y][x] != 9 and [x, y] not in seen]
    for coord in adj_no_nines:
        seen.append([x, y])
        basin_arr += find_basin(coord[0], coord[1], cells, seen)
    return basin_arr


def part_2():
    raw_lines = get_lines('./inputs/09.txt')
    width = len(raw_lines[0])
    height = len(raw_lines)
    height_list = [[int(char) for char in line] for line in raw_lines]
    low_points = []
    low_coords = []
    seen = []
    for y in range(height):
        for x in range(width):
            adj = get_adj(x, y, height_list)
            if min(adj) > height_list[y][x]:
                low_points += [height_list[y][x]]
                low_coords.append([x, y])
                seen.append([x, y])
    basin_sizes = []
    for coord in low_coords:
        basin = find_basin(coord[0], coord[1], height_list, seen)
        basin = set(basin)
        basin_sizes.append(len(basin))
    basin_sizes.sort()
    total = 1
    for size in basin_sizes[-3:]:
        total *= size
    print(total)


if __name__ == '__main__':
    part_1()
    part_2()
