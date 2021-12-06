import re

from AoC import get_lines


class FishPool:
    def __init__(self):
        self.fish = []

    def add(self, fish):
        self.fish.append(fish)

    def __repr__(self) -> str:
        return len(self.fish)


class LanternFish:
    def __init__(self, days):
        self.days = int(days)

    def pass_day(self):
        self.days -= 1

    def reset(self):
        self.days = 6

    def __repr__(self) -> str:
        return f'{self.days}'


def part_1():
    raw_lines = get_lines('./inputs/06.txt')
    pool: list(LanternFish) = [LanternFish(num) for num in raw_lines[0].strip().split(',')]
    days = 80
    for day in range(days):
        for fish in pool:
            fish.pass_day()
            if fish.days < 0:
                fish.reset()
                pool.append(LanternFish(9))

    print(len(pool))


def part_2():
    raw_lines = get_lines('./inputs/06-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()
