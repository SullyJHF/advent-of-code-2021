import os


def get_lines(filename="input.txt", sep='\n'):
    with open(filename) as file:
        return file.read().strip().split(sep)
