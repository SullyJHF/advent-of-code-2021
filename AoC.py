import os
import sys

import requests


def get_lines(filename="input.txt", sep='\n'):
    with open(filename) as file:
        return file.read().strip().split(sep)


def get_input(day: int):
    print(f'Getting day {day} input...')
    with open('./session_cookie') as file:
        cookie = file.read().strip()
    result = requests.get(
        f'https://adventofcode.com/2021/day/{day}/input',
        headers={'Cookie': f'session={cookie}'})
    result.raise_for_status()
    print('Retrieved successfully!')
    input_file = f'./inputs/{str(day).zfill(2)}.txt'
    print(f'Writing to {input_file}')
    with open(input_file, 'x') as file:
        file.write(result.text)
    with open(f'./inputs/{str(day).zfill(2)}-test.txt', 'x') as file:
        file.write('')


if __name__ == '__main__':
    get_input(sys.argv[1])
