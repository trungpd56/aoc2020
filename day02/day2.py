#!/usr/bin/env python3

import pathlib
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def is_valid(line: str, p2: bool = False) -> bool:
    low, high, char, pw = re.split(r"[-: ]\s?", line)
    low, high = map(int, (low, high))
    if not p2:
        return low <= pw.count(char) <= high
    if p2:
        return (pw[low - 1] == char) != (pw[high - 1] == char)


def solution(data):
    """Solve part 1."""
    cnt = 0
    cnt2 = 0
    for line in data:
        cnt += is_valid(line)
        cnt2 += is_valid(line, p2=True)
    return cnt, cnt2


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1, solution2 = solution(data)

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
