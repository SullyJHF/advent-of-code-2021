from functools import cache
from typing import Counter

from AoC import get_lines


def get_data(file):
    raw_lines = get_lines(file)
    players = [int(start) for start in [line.split(': ')[1] for line in raw_lines]]
    return players


def part_1(players):
    score_max = 1000
    dice_value = 1
    player_index = 0
    scores = [0 for p in players]
    roll_count = 0
    while all([score < score_max for score in scores]):
        dice_roll = 0
        for i in range(3):
            roll_count += 1
            dice_roll += dice_value
            dice_value += 1
            # don't need to mod 100 because rolling a 101 is the same as rolling a 1
            # if dice_value > 100:
            #     dice_value %= 100

        players[player_index] += dice_roll
        players[player_index] = (((players[player_index] - 1) % 10) + 1)
        scores[player_index] += players[player_index]

        player_index += 1
        player_index %= 2
    print(min(scores) * roll_count)


# brute force solutions but with cached results for same inputs
# 10 * 10 * 21 * 21 possible cache values
@cache
def play_game(pos1, pos2, score1=0, score2=0):
    if score2 >= 21:
        return 0, 1
    wins1, wins2 = 0, 0

    for roll, count in get_dice_rolls():
        pos1_ = (((pos1 + roll - 1) % 10) + 1)
        # flip pos1, pos2 and score1, score2 to switch players
        w2, w1 = play_game(pos2, pos1_, score2, score1 + pos1_)
        wins1, wins2 = wins1 + count * w1, wins2 + count * w2
    return wins1, wins2


@cache
def get_dice_rolls():
    counter = Counter()
    for x, y, z in [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)]:
        counter[x + y + z] += 1
    return list(counter.items())


def part_2(players):
    print(max(play_game(players[0], players[1])))


if __name__ == '__main__':
    players = get_data('./inputs/21.txt')
    part_1(players)
    players = get_data('./inputs/21.txt')
    part_2(players)
