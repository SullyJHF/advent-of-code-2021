from collections import defaultdict

from AoC import get_lines


def navigate(cave_map, twice):
    def count_next_paths(cave_name, visited, twice):
        if cave_name.islower():
            visited = visited.union({cave_name})
        paths = 0
        for child in cave_map[cave_name]:
            if child == 'end':
                paths += 1
            elif child not in visited:
                paths += count_next_paths(child, visited, twice)
            elif child != 'start' and twice:
                paths += count_next_paths(child, visited, False)
        return paths
    return count_next_paths('start', frozenset(), twice)


def part_1():
    raw_lines = get_lines('./inputs/12.txt')
    cave_map = defaultdict(list)
    for line in raw_lines:
        a, b = line.split("-")
        cave_map[a].append(b)
        cave_map[b].append(a)

    paths = navigate(cave_map, False)
    print(paths)


def part_2():
    raw_lines = get_lines('./inputs/12.txt')
    cave_map = defaultdict(list)
    for line in raw_lines:
        a, b = line.split("-")
        cave_map[a].append(b)
        cave_map[b].append(a)

    paths = navigate(cave_map, True)
    print(paths)


if __name__ == '__main__':
    part_1()
    part_2()
