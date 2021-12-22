from collections import defaultdict
from typing import Counter

from AoC import get_lines


class Cuboid:
    def __init__(self, line) -> None:
        parts = line.split(' ')
        self.instr = parts[0]
        self.coords = [tuple([int(y) for y in x[2:].split('..')]) for x in parts[1].split(',')]
        self.small = (
            self.coords[0][0] >= -50 and self.coords[0][1] <= 50
        ) and (
            self.coords[1][0] >= -50 and self.coords[1][1] <= 50
        ) and (
            self.coords[2][0] >= -50 and self.coords[0][1] <= 50
        )

    def apply_to_points(self, points):
        for x in range(self.coords[0][0], self.coords[0][1] + 1):
            for y in range(self.coords[1][0], self.coords[1][1] + 1):
                for z in range(self.coords[2][0], self.coords[2][1] + 1):
                    points[(x, y, z)] = 1 if self.instr == 'on' else 0


def parse_data(raw_lines) -> list('Cuboid'):
    steps = []
    for line in raw_lines:
        steps.append(Cuboid(line))
    return steps


def get_points_in_cuboid(cuboid: Cuboid):
    points = defaultdict(int)
    for x in range(cuboid.coords[0][0], cuboid.coords[0][1] + 1):
        for y in range(cuboid.coords[1][0], cuboid.coords[1][1] + 1):
            for z in range(cuboid.coords[2][0], cuboid.coords[2][1] + 1):
                points[(x, y, z)] = 1
    return points


def get_min_max_points(cuboids):
    mins = [9999999, 9999999, 9999999]
    maxes = [0, 0, 0]
    print(cuboids)
    for cuboid in cuboids:
        print(cuboid)
        if cuboid.coords[0][0] < mins[0]:
            mins[0] = cuboid.coords[0][0]
        if cuboid.coords[1][0] < mins[1]:
            mins[1] = cuboid.coords[1][0]
        if cuboid.coords[2][0] < mins[2]:
            mins[2] = cuboid.coords[2][0]

        if cuboid.coords[0][1] > maxes[0]:
            maxes[0] = cuboid.coords[0][1]
        if cuboid.coords[1][1] > maxes[1]:
            maxes[1] = cuboid.coords[1][1]
        if cuboid.coords[2][1] > maxes[2]:
            maxes[2] = cuboid.coords[2][1]
    return mins, maxes


def part_1():
    raw_lines = get_lines('./inputs/22.txt')
    cuboids: list(Cuboid) = parse_data(raw_lines)
    points = defaultdict(int)
    for cuboid in [cuboid for cuboid in cuboids if cuboid.small]:
        cuboid.apply_to_points(points)
    print(Counter(points.values()))


def part_2():
    raw_lines = get_lines('./inputs/22-test.txt')
    cuboids: list(Cuboid) = parse_data(raw_lines)
    points = get_points_in_cuboid(cuboids[0])
    print(len(points))


if __name__ == '__main__':
    part_1()
    part_2()
