#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n\n")


def part1(data):
    """Solve part 1."""
    cnt = 0
    for line in data:
        cnt += len(set(line.replace("\n", "")))
    return cnt


def part2(data):
    """Solve part 2."""
    cnt = 0
    for line in data:
        num = line.count('\n') + 1
        for c in set(line.replace("\n", "")):
            if line.count(c) == num:
                cnt += 1
    return cnt


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
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
