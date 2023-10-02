#!/usr/bin/env python3

import pathlib
import sys
import math
from functools import reduce


def parse(puzzle_input):
    """Parse input."""
    time, raw = puzzle_input.split()
    busid = [int(tok) if tok.isdigit() else tok for tok in raw.split(",")]
    return int(time), busid


def part1(data):
    """Solve part 1."""
    time, busid = data
    wait = [(bus, bus - (time % bus)) for bus in busid if isinstance(bus, int)]
    swait = sorted(wait, key=lambda x: (x[1], x[0]))
    return math.prod(swait[0])


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part2(data):
    """Solve part 2.
    (t+i) ≡ 0 mod b
    t ≡ -i mod b
    t ≡ b-i mod b
    """
    busid = [int(tok) if tok.isdigit() else tok for tok in data.split(",")]
    remain = [int(b) - i for i, b in enumerate(busid) if b != "x"]
    bus = [b for b in busid if b != "x"]
    return chinese_remainder(bus, remain)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    puzzle_input = puzzle_input.split("\n")[1]
    solution2 = part2(puzzle_input)

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
