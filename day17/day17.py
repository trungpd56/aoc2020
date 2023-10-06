#!/usr/bin/env python3

import pathlib
import sys
from itertools import product


def bound(grid, d=3):
    res = []
    for i in range(d):
        mind = min(grid, key=lambda x: x[i])[i] - 1
        maxd = max(grid, key=lambda x: x[i])[i] + 2
        res.append((mind, maxd))
    return res


def cnt(point, grid):
    dim = len(point)
    diffs = product((-1, 0, 1), repeat=dim)
    return sum(
        [
            tuple(n1 + n2 for n1, n2 in zip(point, d)) in grid
            for d in diffs
            if d != tuple([0] * dim)
        ]
    )


def parse(puzzle_input):
    """Parse input."""
    grid = set()
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == "#":
                grid.add((x, y, 0, 0))
    return grid


def solution(data, d=3):
    """Solve part 1."""
    for _ in range(6):
        bounds = bound(data, d)
        ndata = set()
        wrange = [0] if d == 3 else range(*bounds[3])
        for x in range(*bounds[0]):
            for y in range(*bounds[1]):
                for z in range(*bounds[2]):
                    for w in wrange:
                        ncount = cnt((x, y, z, w), data)
                        if (x, y, z, w) in data and ncount in (2, 3):
                            ndata.add((x, y, z, w))
                        elif (x, y, z, w) not in data and ncount == 3:
                            ndata.add((x, y, z, w))
        data = ndata
    return len(data)


def part2(data):
    """Solve part 2."""
    """Can copy the above function with added parameter w at the end"""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, d=4)

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
