from collections import defaultdict

from AoC import get_lines

matching_symbols = {
    '}': '{',
    '>': '<',
    ')': '(',
    ']': '[',
}
symbol_weights = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def process_corrupted(line):
    total = 0
    open_symbols = []
    for char in line:
        if char == '{' or char == '(' or char == '<' or char == '[':
            open_symbols.append(char)
        else:
            open_symbol = open_symbols.pop()
            if matching_symbols[char] != open_symbol:
                total += symbol_weights[char]

    return total
    # print(symbols['{'] - symbols['}'])
    # print(symbols['('] - symbols[')'])
    # print(symbols['<'] - symbols['>'])
    # print(symbols)


def part_1():
    raw_lines = get_lines('./inputs/10.txt')
    total = 0
    for line in raw_lines:
        total += process_corrupted(line)
    print(total)


def part_2():
    raw_lines = get_lines('./inputs/10-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()
