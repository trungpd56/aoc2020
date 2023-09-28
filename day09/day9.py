#!/usr/bin/env python3

import pathlib
import sys
from itertools import combinations
from typing import List


def parse(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.splitlines()]


def part1(data: List[int], n: int = 25) -> int:
    """Solve part 1."""
    for i in range(n, len(data)):
        combs = combinations(data[i - n : i], 2)
        num = data[i]
        if any(num == sum(c) for c in combs):
            continue
        return num
    return 0


def part2(data: List[int], num: int) -> int:
    """Solve part 2."""
    for i in range(2, len(data)):
        for j in range(i):
            nrange = data[j:i]
            if sum(nrange) == num:
                return max(nrange) + min(nrange)
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data, num=solution1)

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
