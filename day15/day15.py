#!/usr/bin/env python3

import pathlib
import sys
from collections import defaultdict, deque


def parse(puzzle_input):
    """Parse input."""
    return list(map(int, puzzle_input.split(",")))


def solution(data, time=2020):
    """Solve part 1."""
    lturn = defaultdict(lambda: deque(maxlen=2))
    for i, n in enumerate(data, 1):
        lturn[n].append(i)
    cnum = data[-1]
    cturn = len(data)
    while True:
        if len(lturn[cnum]) < 2:
            nnum = 0
        else:
            nnum = lturn[cnum][1] - lturn[cnum][0]
        cturn += 1
        lturn[nnum].append(cturn)
        cnum = nnum
        if cturn == time:
            return nnum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, 30000000)

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
