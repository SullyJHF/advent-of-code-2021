import re

from AoC import get_lines


def part_1():
    lines = get_lines('./inputs/03.txt')
    width = len(lines[0])
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(width):
        num_ones = len([line for line in lines if line[i] == '1'])

        num_zeroes = len(lines) - num_ones
        if (num_ones > num_zeroes):
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


def part_2():
    raw_lines = get_lines('./inputs/03.txt')

    def find_num(lines, i, greater):
        if len(lines) == 1:
            return lines[0]
        if i >= len(lines[0]):
            return lines[-1]
        one_list = [line for line in lines if line[i] == '1']
        zero_list = [line for line in lines if line[i] == '0']
        num_ones = len(one_list)
        num_zeroes = len(zero_list)

        if not greater:
            zero_list, one_list = one_list, zero_list

        if num_ones >= num_zeroes:
            return find_num(one_list, i + 1, greater)
        else:
            return find_num(zero_list, i + 1, greater)
    oxygen = find_num(raw_lines, 0, True)
    co2 = find_num(raw_lines, 0, False)
    print(int(oxygen, 2) * int(co2, 2))


if __name__ == '__main__':
    part_1()
    part_2()
