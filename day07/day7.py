#!/usr/bin/env python3

import pathlib
import sys
import re
from collections import defaultdict


def parse(puzzle_input):
    """Parse input."""
    info = defaultdict(dict)
    for line in puzzle_input.splitlines():
        toks = re.split(r"\scontain\s|,\s", line)
        name = toks[0].replace(" bags", "")
        for t in toks[1:]:
            if "no other" in t:
                info[name] = {}
            else:
                t = t.split()
                info[name][" ".join(t[1:3])] = int(t[0])
    return info


def valid(obag: str, ibag: str, info: dict) -> bool:
    if ibag in info[obag]:
        return True
    else:
        return any(valid(b, ibag, info) for b in info[obag])


def cnt_bags(bag: str, info: dict) -> int:
    if not info[bag]:
        return 0
    cnt = 0
    for b in info[bag]:
        cnt += info[bag][b] + info[bag][b] * cnt_bags(b, info)
    return cnt


def part1(data):
    """Solve part 1."""
    cnt = 0
    for b in data:
        cnt += valid(b, "shiny gold", data)
    return cnt


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = cnt_bags("shiny gold", data)

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
