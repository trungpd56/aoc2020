#!/usr/bin/env python3

import pathlib
import sys
import re
from collections import defaultdict
from itertools import product


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.splitlines()


def part1(data):
    """Solve part 1."""
    info = defaultdict(int)
    for line in data:
        if line.startswith("mask"):
            mask = line.split()[-1]
        else:
            add, val = map(int, re.findall(r"\d+", line))
            res = "".join([v if m == "X" else m for m, v in zip(mask, f"{val:036b}")])
            info[add] = int(res, 2)
    return sum(info.values())


def genadd(s):
    xcount = s.count("X")
    adds = []
    for mul in product(["0", "1"], repeat=xcount):
        ns = s
        for c in mul:
            ns = ns.replace("X", c, 1)
        adds.append(int(ns, 2))
    return adds


def part2(data):
    """Solve part 2."""
    info = defaultdict(int)
    for line in data:
        if line.startswith("mask"):
            mask = line.split()[-1]
        else:
            add, val = map(int, re.findall(r"\d+", line))
            res = "".join(
                [m if m == "X" or m == "1" else v for m, v in zip(mask, f"{add:036b}")]
            )
            for a in genadd(res):
                info[a] = val
    return sum(info.values())


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
