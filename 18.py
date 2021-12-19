
import ast

from defaultlist import defaultlist
from numpy import deprecate_with_doc, number

from AoC import get_lines


def explode_snailfish(snailfish: list[int], depth=0):
    string_fish = str(snailfish).replace(' ', '')
    depth = 0
    deep_index = None
    deep_index_end = None
    to_explode = []
    explode_string = ''
    for i, char in enumerate(string_fish):
        if char == '[':
            depth += 1
            continue
        elif char == ']':
            depth -= 1
            continue
        elif char == ',':
            continue

        if depth >= 5:
            deep_index = i
            count = i
            while char != ']':
                count += 1
                explode_string += char
                char = string_fish[count]
                deep_index_end = count
            deep_index_end -= 1
            break
            # if not deep_index:
            #     deep_index = i
            # else:
            #     deep_index_end = i
            # to_explode.append(int(char))

        # if len(to_explode) == 2:
        #     break
    to_explode = [int(char) for char in explode_string.split(',')]
    # print(explode_string)
    # print(string_fish)
    # print(to_explode)

    # TODO: handle multiple digits here too
    left_index = None
    right_index = None
    for i, char in enumerate(string_fish[:deep_index]):
        if char.isnumeric():
            left_index = i
    for i, char in enumerate(string_fish[deep_index_end + 1:]):
        if char.isnumeric():
            right_index = i + deep_index_end + 1
            break

    string_fish_array = list(string_fish)
    if left_index:
        num = string_fish[left_index]
        # print(num)
        length = 0
        if string_fish[left_index - 1].isnumeric():
            num = string_fish[left_index - 1] + num
            left_index -= 1
            length = 1
        # print(left_index, length, num)
        # print(string_fish_array[0:1])
        string_fish_array[left_index] = str(int(num) + to_explode[0])
        if length > 0:
            string_fish_array.pop(left_index + length)
            deep_index -= length
            deep_index_end -= length
            if right_index:
                right_index -= length
    #     print(string_fish_array)
    # print(string_fish_array)
    # print(string_fish)
    if right_index:
        # print(string_fish[right_index + 1])
        num = string_fish_array[right_index]
        # right_index -= length
        # print(string_fish_array[right_index])
        length = 0
        if string_fish_array[right_index + 1].isnumeric():
            num = num + string_fish_array[right_index + 1]
            # right_index -= 1
            length = 1

        string_fish_array[right_index] = str(int(num) + to_explode[1])
        # print(string_fish_array[right_index])
        if length > 0:
            string_fish_array.pop(right_index + length)
            # deep_index -= length
            # deep_index_end -= length
    # print(string_fish_array[deep_index - 1: deep_index_end + 2])
    string_fish_array[deep_index - 1:deep_index_end + 2] = '0'
    string_fish = ''.join(string_fish_array)
    # print(string_fish)
    return ast.literal_eval(string_fish)


def test_explode():
    assert explode_snailfish([[[[[9, 8], 1], 2], 3], 4]) == [[[[0, 9], 2], 3], 4]
    assert explode_snailfish([[[[[9, 9], 2], 2], 3], 4]) == [[[[0, 11], 2], 3], 4]
    assert explode_snailfish([7, [6, [5, [4, [3, 2]]]]]) == [7, [6, [5, [7, 0]]]]
    assert explode_snailfish([7, [6, [5, [4, [7, 2]]]]]) == [7, [6, [5, [11, 0]]]]
    assert explode_snailfish([[6, [5, [4, [3, 2]]]], 1]) == [[6, [5, [7, 0]]], 3]
    assert explode_snailfish([[6, [5, [4, [9, 9]]]], 1]) == [[6, [5, [13, 0]]], 10]
    assert explode_snailfish(
        [[3, [2, [1, [7, 3]]]],
         [6, [5, [4, [3, 2]]]]]) == [
        [3, [2, [8, 0]]],
        [9, [5, [4, [3, 2]]]]]
    assert explode_snailfish([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]) == [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
    assert explode_snailfish([[[[12, 12], [6, 14]], [[15, 0], [17, [8, 1]]]], [2, 9]]) == [
        [[[12, 12], [6, 14]], [[15, 0], [25, 0]]], [3, 9]]
    # assert explode_snailfish([[[[4, 0], [5, 4]], [[7, 0], [15, 5]]], [10, [[0, [11, 3]], [[6, 3], [8, 8]]]]]) == [
    #     [[[4, 0], [5, 4]], [[7, 0], [15, 5]]], [10, [[0, [11, 3]], [[6, 3], [8, 8]]]]]


def add_snailfish(pair_a: list[int], pair_b: list[int]):
    return [pair_a, pair_b]


def split_snailfish(snailfish: list[int]):
    string_fish = str(snailfish).replace(' ', '')
    last_char = None
    for i, char in enumerate(string_fish):
        if char.isnumeric():
            if last_char and last_char.isnumeric():
                num = int(last_char + char)
                left = num // 2
                right = num // 2 + num % 2
                string_fish_array = list(string_fish)
                string_fish_array[i - 1:i + 1] = f'[{left},{right}]'
                string_fish = ''.join(string_fish_array)
                return ast.literal_eval(string_fish)
            last_char = char
        else:
            last_char = None


def test_split():
    assert split_snailfish([[[[0, 7], 4], [15, [0, 13]]], [1, 1]]) == [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    assert split_snailfish([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]) == [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]


def do_what(snailfish):
    string_fish = str(snailfish).replace(' ', '')
    depth = 0
    for i, char in enumerate(string_fish):
        if char == '[':
            depth += 1
            continue
        elif char == ']':
            depth -= 1
            continue
        elif char == ',':
            continue
        if depth == 5:
            return 'explode'

    last_char = None
    for i, char in enumerate(string_fish):
        if char.isnumeric():
            if last_char and last_char.isnumeric():
                return 'split'
            last_char = char
        else:
            last_char = None
    return 'nothing'


def magnitude(snailfish: list[int]):
    string_fish = str(snailfish).replace(' ', '')
    depth = 0
    e_i = 0
    to_explode = defaultlist(str)
    for i, char in enumerate(string_fish):
        if char == '[':
            depth += 1
            continue
        elif char == ']':
            to_explode[depth] += ';'
            depth -= 1
            e_i += 1
            continue
        to_explode[depth] += char
    x = []
    for nums in to_explode:
        x += nums.split(';')
    mags = defaultlist(int)
    done_nums = []
    for explode in x:
        nums = [int(num) for num in explode.split(',') if num]
        if len(nums) != 2:
            continue
        done_nums.append(nums)
        mags.append(3 * nums[0] + 2 * nums[1])
    string_fish_array = list(string_fish)
    for i in range(len(done_nums), 0, -1):
        string_fish_array = list(string_fish)
        num_string = ','.join([str(num) for num in done_nums[i - 1]])
        index = string_fish.rindex(num_string)

        string_fish_array = string_fish_array[0:index - 1] + [
            str(mags[i - 1])] + string_fish_array[index + len(num_string) + 1:]
        string_fish = ''.join(string_fish_array)
    if '[' in ''.join(string_fish_array):
        return magnitude(ast.literal_eval(''.join(string_fish_array)))
    return int(string_fish_array[0])


def test_magnitude():
    assert magnitude([[1, 2], [[3, 4], 5]]) == 143
    assert magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]) == 1384
    assert magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]) == 3488
    assert magnitude([[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]]) == 4140


def part_1():
    raw_lines = get_lines('./inputs/18.txt')
    test_explode()
    test_split()
    test_magnitude()
    snailfish = ast.literal_eval(raw_lines[0])
    for line in raw_lines[1:]:
        snailfish = add_snailfish(snailfish, ast.literal_eval(line))
        what = do_what(snailfish)
        while what != 'nothing':
            if what == 'explode':
                snailfish = explode_snailfish(snailfish)
            elif what == 'split':
                snailfish = split_snailfish(snailfish)
            what = do_what(snailfish)
    print(snailfish)
    print(magnitude(snailfish))


def part_2():
    raw_lines = get_lines('./inputs/18-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()
