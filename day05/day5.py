#!/usr/bin/env python3

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def seat(line: str) -> int:
    tok = line.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    return int(tok, 2)


def part1(data):
    """Solve part 1."""
    return max(seat(line) for line in data)


def part2(data):
    """Solve part 2."""
    all_seats = set(range(1024))
    occupied_seat = set(seat(line) for line in data)
    free_seat = all_seats - occupied_seat
    yours = [s for s in free_seat if s - 1 not in free_seat and s + 1 not in free_seat]
    return yours[0]


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
