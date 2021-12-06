import re
from collections import Counter, defaultdict

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
    days = 256
    raw_lines = get_lines('./inputs/06.txt')
    pool = [int(num) for num in raw_lines[0].strip().split(',')]

    age_dict = defaultdict(int)
    # construct dict of age:count
    for fish_age in pool:
        age_dict[fish_age] += 1

    for day in range(days):
        temp_age_dict = defaultdict(int)
        for age, count in age_dict.items():
            if age == 0:
                # if age is 0 then add count to 6 day old and 8 day old counts
                temp_age_dict[6] += count
                temp_age_dict[8] += count
            else:
                # otherwise add count to each other fish age
                temp_age_dict[age - 1] += count
        # set new age dict to the calculated one
        age_dict = temp_age_dict
    print(sum(age_dict.values()))


if __name__ == '__main__':
    part_1()
    part_2()
