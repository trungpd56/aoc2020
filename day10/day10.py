#!/usr/bin/env python3

import pathlib
import sys
from typing import List


def parse(puzzle_input):
    """Parse input."""
    data = [int(line) for line in puzzle_input.splitlines()]
    return sorted(data + [0] + [max(data) + 3])


def part1(data):
    """Solve part 1."""
    diffs = [data[i] - data[i - 1] for i in range(1, len(data))]
    return diffs.count(1) * diffs.count(3)


def part2(path: List[int], data: List[int], cache: dict=None) -> int:
    """The solution for this part is not good, just to understand recursive"""
    if cache is None:
        cache = {}

    if path[-1] == max(data):
        return 1

    if (key := tuple(path)) in cache:
        return cache[key]

    cnt = 0
    for p in data:
        if 1 <= p - path[-1] <= 3:
            # print(path, p)
            cnt += part2(path + [p], data, cache)
    cache[key] = cnt
    return cnt



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2([0], data)

    return solution1, solution2


if __name__ == "__main__":
    infile = (
        sys.argv[1]
        if len(sys.argv) > 1
        else pathlib.Path(__file__).parent / "input.txt"
    )
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
