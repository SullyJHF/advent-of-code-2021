import re

from AoC import get_lines


def part_1():
    raw_lines = get_lines('./inputs/07.txt')
    x = [int(num) for num in raw_lines[0].strip().split(',')]
    r = max(x) - min(x)
    min_fuel = 9999999
    fuel_val = 0
    fuel_used = max(x)
    for i in range(r):
        fuel_used = 0
        for hor_pos in x:
            fuel_used += abs(hor_pos - i)
        if fuel_used < min_fuel:
            min_fuel = fuel_used
            fuel_val = i
    print(fuel_val, min_fuel)


def part_2():
    raw_lines = get_lines('./inputs/07.txt')
    x = [int(num) for num in raw_lines[0].strip().split(',')]
    r = max(x) - min(x)
    min_fuel = 999999999999
    fuel_val = 0
    fuel_used = max(x)
    for i in range(r):
        fuel_used = 0
        for hor_pos in x:
            d = abs(hor_pos - i)
            fuel_used += int(d * (d + 1) / 2)
        if fuel_used < min_fuel:
            min_fuel = fuel_used
            fuel_val = i
    print(fuel_val, min_fuel)


if __name__ == '__main__':
    part_1()
    part_2()
