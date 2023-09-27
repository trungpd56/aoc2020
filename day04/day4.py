#!/usr/bin/env python3

import pathlib
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    return [raw for raw in puzzle_input.split("\n\n")]


def valid(raw: str, p2: bool = False) -> bool:
    fields = {
        "byr": r"(19\d\d|200[12])",
        "iyr": r"(201\d|2020)",
        "eyr": r"(202\d|2030)",
        "hgt": r"((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)",
        "hcl": r"#\w{6}",
        "ecl": r"(amb|blu|brn|gry|grn|hzl|oth)",
        "pid": r"\b\d{9}\b",
    }
    toks = re.split(r"[ \n:]", raw)
    if all(f in toks[::2] for f in fields):
        if not p2:
            return True
        elif all(
            re.search(fields[k], v) for k, v in zip(toks[::2], toks[1::2]) if k != "cid"
        ):
            return True
    return False


def part1(data):
    """Solve part 1."""
    cnt = 0
    for raw in data:
        cnt += valid(raw)
    return cnt


def part2(data):
    """Solve part 2."""
    cnt = 0
    for raw in data:
        cnt += valid(raw, p2=True)
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
