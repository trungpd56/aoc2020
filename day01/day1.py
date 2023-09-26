#!/usr/bin/env python3

import pathlib
import sys
from itertools import combinations
import math

def parse(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.splitlines()]

def solution(data, n=2):
    """Solve part 1."""
    pair = [p for p in combinations(data, n) if sum(p) == 2020][0]
    return math.prod(pair)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, n=3)

    return solution1, solution2

if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent / "input.txt"
    puzzle_input = pathlib.Path(infile).read_text().strip()
    solution1, solution2 = solve(puzzle_input)
    if solution1:
        print(f" part1: {solution1}")
    if solution2:
        print(f" part2: {solution2}")
