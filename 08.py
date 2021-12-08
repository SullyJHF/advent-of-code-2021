from AoC import get_lines


def part_1():
    raw_lines = get_lines('./inputs/08.txt')
    x = [line.split('|') for line in raw_lines]
    total = 0
    for segment in x:
        digits = segment[1].strip().split(' ')
        total += len([digit for digit in digits if len(digit) == 2 or len(
            digit) == 4 or len(digit) == 3 or len(digit) == 7])
    print(total)


def part_2():
    raw_lines = get_lines('./inputs/08.txt')
    x = [line.split('|') for line in raw_lines]
    total = 0
    for line in x:
        segment_mappings = []
        segments = line[0].strip().split(' ')
        digits = line[1].strip().split(' ')
        one = [segment for segment in segments if len(segment) == 2][0]
        four = [segment for segment in segments if len(segment) == 4][0]
        seven = [segment for segment in segments if len(segment) == 3][0]
        eight = [segment for segment in segments if len(segment) == 7][0]
        remaining_two_letters = set([letter for letter in eight if letter not in one + four + seven])
        six_length_segments = [segment for segment in segments if len(segment) == 6]

        for segment in six_length_segments:
            if all([True if char in segment else False for char in one]):
                if all([True if char in segment else False for char in remaining_two_letters]):
                    zero = segment
                else:
                    nine = segment
            else:
                six = segment

        five_length_segments = [segment for segment in segments if len(segment) == 5]
        for segment in five_length_segments:
            if all([True if char in segment else False for char in one]):
                three = segment
            elif all([True if char in segment else False for char in remaining_two_letters]):
                two = segment
            else:
                five = segment

        segment_mappings = [
            ''.join(sorted(zero)),
            ''.join(sorted(one)),
            ''.join(sorted(two)),
            ''.join(sorted(three)),
            ''.join(sorted(four)),
            ''.join(sorted(five)),
            ''.join(sorted(six)),
            ''.join(sorted(seven)),
            ''.join(sorted(eight)),
            ''.join(sorted(nine)),
        ]

        result = ''
        for digit_segment in digits:
            sorted_digit = ''.join(sorted(digit_segment))
            result += str(segment_mappings.index(sorted_digit))
        total += int(result)
    print(total)


if __name__ == '__main__':
    part_1()
    part_2()
