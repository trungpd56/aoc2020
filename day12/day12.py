#!/usr/bin/env python3

import pathlib
import sys
import math


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    dir = 90
    x, y = 0, 0
    for line in data:
        val = int(line[1:])
        match line[0]:
            case "N":
                y += val
            case "S":
                y -= val
            case "E":
                x += val
            case "W":
                x -= val
            case "R":
                dir = (dir + val) % 360
            case "L":
                dir = (dir - val) % 360
            case "F":
                y += round(math.cos(math.radians(dir)) * val)
                x += round(math.sin(math.radians(dir)) * val)
    return abs(x) + abs(y)


def part2(data):
    """Solve part 2."""


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
