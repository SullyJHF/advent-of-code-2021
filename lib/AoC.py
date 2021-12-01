import os


def get_lines(dir, filename="input.txt", sep='\n'):
    here = os.path.dirname(os.path.abspath(dir))
    filepath = os.path.join(here, filename)

    contents = None
    with open(filepath) as file:
        contents = file.read().strip()
    return contents.split(sep)
