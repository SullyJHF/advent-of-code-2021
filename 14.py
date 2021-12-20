import re
from collections import defaultdict
from typing import Counter

from AoC import get_lines


def get_data():
    raw_lines = get_lines('./inputs/14.txt', '\n\n')
    template = list(raw_lines[0])
    rules = defaultdict(str)
    for line in raw_lines[1].splitlines():
        x = line.split(' -> ')
        rules[x[0]] = x[1]
    return template, rules


def part_1():
    template, rules = get_data()
    steps = 10
    for step in range(steps):
        for i in range(len(template) - 2, -1, -1):
            chars = ''.join(template[i:i + 2])
            if chars in rules:
                template = template[:i] + [chars[0], rules[chars], chars[1]] + template[i + 2:]
    c = Counter(template)
    print(c.most_common()[0][1] - c.most_common()[len(c) - 1][1])


def part_2():
    template, rules = get_data()
    steps = 40
    counter = Counter()
    for i in range(len(template) - 1):
        counter[template[i] + template[i + 1]] += 1
    for i in range(steps):
        new_pairs = Counter()
        for pair in counter:
            new_pairs[pair[0] + rules[pair]] += counter[pair]
            new_pairs[rules[pair] + pair[1]] += counter[pair]
        counter = new_pairs
    letters = Counter()
    for pair in counter:
        letters[pair[0]] += counter[pair]
    letters[template[-1]] += 1
    print(letters.most_common()[0][1] - letters.most_common()[len(letters) - 1][1])


if __name__ == '__main__':
    part_1()
    part_2()
