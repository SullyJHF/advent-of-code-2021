from AoC import get_lines

global version
version = 0


def parse_literal_packet(bits, pointer):
    # print('literal value parsing')
    # print(bits)
    indiciator_bit = bits[pointer]
    pointer += 1
    value_bits = bits[pointer:pointer + 4]
    pointer += 4
    # print(value_bits)

    while indiciator_bit == '1':
        indiciator_bit = bits[pointer]
        pointer += 1
        value_bits += bits[pointer:pointer + 4]
        pointer += 4
        # print(value_bits)
    # print(value_bits)
    # print(bits[pointer:])
    # return (int(value_bits, 2), bits[pointer:])
    return pointer
    # if not all([True if char == '0' else False for char in bits[pointer:]]):
    # return int(value_bits, 2), False


def parse_operator_packet(bits, pointer):
    # print('operator packet parsing')
    # print(f'{pointer=}')
    length_type = bits[pointer]
    # print(f'{length_type=}')
    pointer += 1
    length = 0
    leftovers = False
    if length_type == '0':
        length = int(bits[pointer:pointer + 15], 2)
        pointer += 15
        # print(f'{length=}')
        # pointer += length
        # print(bits[pointer:pointer + length])
    elif length_type == '1':
        # parse this NUMBER of sub packets, not bit length
        num_packets = int(bits[pointer:pointer + 11], 2)
        # print(f'{num_packets=}')
        pointer += 11
        for i in range(num_packets):
            pointer = parse_packet(bits, pointer)
            # pointer += len(leftovers)
    return pointer
    # want to return sub packets
    return leftovers or bits[pointer:pointer + length]
    # parse_packet(bits)


def parse_packet(bits, pointer):
    # print(f'{pointer}')
    packet_version = int(bits[pointer:pointer + 3], 2)
    packet_type = int(bits[pointer + 3:pointer + 6], 2)
    global version
    version += packet_version
    print(f'{packet_version=}')
    # print(f'{packet_type=}')
    pointer += 6
    # print(f'{packet_type=}')

    if packet_type == 4:
        pointer = parse_literal_packet(bits, pointer)
    else:
        pointer = parse_operator_packet(bits, pointer)

    return pointer


def part_1():
    raw_lines = get_lines('./inputs/16.txt')
    hex_string = raw_lines[0]
    binary_string = ''.join([bin(int(char, 16))[2:].zfill(4) for char in hex_string])
    print(binary_string)
    pointer = parse_packet(binary_string, 0)
    # print(pointer)
    # print(len(binary_string))
    # print(pointer)
    while (len(binary_string) - pointer) > 4 and not all(True if char == '0' else False for char in binary_string[pointer:]):
        pointer = parse_packet(binary_string, pointer)
    print(version)

    # pointer = 0
    # packet_version = int(binary_string[pointer:pointer + 3], 2)
    # packet_type = int(binary_string[pointer + 3:pointer + 6], 2)
    # print(f'{packet_version=}')
    # print(f'{packet_type=}')
    # # print(f'{packet_data=}')
    # pointer += 6
    # if packet_type == 4:
    #     pass
    #     # pointer_offset = parse_literal_packet(packet_data)
    # else:
    #     length_type = binary_string[pointer]
    #     print(f'{length_type=}')
    #     pointer += 1
    #     if length_type == '0':
    #         length = int(binary_string[pointer:pointer + 15], 2)
    #         pointer += 15
    #         print(f'{length=}')
    #         pointer += length
    #         print(binary_string[pointer:pointer + length])
    #     elif length_type == '1':
    #         # parse this NUMBER of sub packets, not bit length
    #         num_packets = int(binary_string[pointer:pointer + 11], 2)
    #         print(f'{num_packets=}')
    #         pointer += 11
    #         for i in range(num_packets):
    #             print(f'{i=}')
    #             packet_version = int(binary_string[pointer:pointer + 3], 2)
    #             packet_type = int(binary_string[pointer + 3:pointer + 6], 2)
    #             pointer += 6
    #             print(f'{packet_version=}')
    #             print(f'{packet_type=}')
    # pointer += parse_packet(leftovers, 0)

    # print(f'{leftovers=}')
    # pointer += len(leftovers)

    # total_version_nums = value
    # while leftovers:
    #     # print(leftovers)
    #     value, leftovers = parse_packet(leftovers)
    #     total_version_nums += value
    # print(total_version_nums)

    # print(packet_version)
    # print(packet_type)


def part_2():
    raw_lines = get_lines('./inputs/16-test.txt')


if __name__ == '__main__':
    part_1()
    part_2()


# 0000000001010100000000000000000001011000010001010110100010111000001000000000101111000110000010001101000000
# 110100101111111000101000
# 00000000000000000101100001000101010110001011001000100000000010000100011000111000110100
