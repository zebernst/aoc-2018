from code import aoc
from code.utils import *


def part1(data: str):
    return Query(data.strip().split('\n')).select(lambda x: x.replace('+', '')).select(lambda x: int(x)).sum()


def part2(data: str):
    digits = Query(data.strip().split('\n')).select(lambda x: x.replace('+', '')).select(lambda x: int(x)).as_list
    i = 0
    past_freq = set()
    freq = 0

    while True:
        past_freq.add(freq)
        freq += digits[i]
        if freq in past_freq:
            break
        i = (i + 1) % len(digits)
    return freq


if __name__ == '__main__':
    data = aoc.data(day=1)

    print("part 1:", part1(data))
    print("part 2:", part2(data))
