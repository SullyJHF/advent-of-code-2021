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
incomplete_weights = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
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


def process_incomplete(line):
    open_symbols = []
    for char in line:
        if char == '{' or char == '(' or char == '<' or char == '[':
            open_symbols.append(char)
        else:
            open_symbols.pop()
    open_symbols.reverse()
    weights = [incomplete_weights[char] for char in open_symbols]
    total = 0
    for weight in weights:
        total *= 5
        total += weight
    return total


def part_1():
    raw_lines = get_lines('./inputs/10.txt')
    total = 0
    for line in raw_lines:
        total += process_corrupted(line)
    print(total)


def part_2():
    raw_lines = get_lines('./inputs/10.txt')
    incomplete_lines = []
    for line in raw_lines:
        if process_corrupted(line) == 0:
            incomplete_lines.append(line)

    scores = [process_incomplete(line) for line in incomplete_lines]
    scores.sort()
    print(scores[len(scores) // 2])


if __name__ == '__main__':
    part_1()
    part_2()
