#!/usr/bin/env python3

import pathlib
import sys
from typing import List
import math


def parse(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def solution(data: List[str], dx: int=3, dy: int=1) -> int:
    """Solve part 1."""
    maxx, maxy = len(data[0]), len(data)
    x, y = 0, 0
    cnt = 0
    while y < maxy:
        if data[y][x] == "#":
            cnt += 1
        x = (x + dx) % maxx
        y += dy
    return cnt


def part2(data):
    """Solve part 2."""
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    res = []
    for dx, dy in slopes:
        res.append(solution(data, dx, dy))
    return math.prod(res)



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = part2(data)

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
