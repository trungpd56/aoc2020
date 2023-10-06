#!/usr/bin/env python3

import pathlib
import sys
import re
import math


class Ticket:
    def __init__(self, lines):
        for line in lines.strip().splitlines():
            name, *nums = re.split(r": |-| or ", line)
            if name == "class":
                name = "class_"
            setattr(self, f"{name}", tuple(map(int, nums)))

    def invalid(self, line):
        for n in line.split(","):
            if all(not Ticket.inrange(n, v) for v in self.__dict__.values()):
                return int(n)
        return 0

    def fields(self, col):
        fields = set()
        for k, v in self.__dict__.items():
            if all(Ticket.inrange(n, v) for n in col):
                fields.add(k)
        return fields

    @staticmethod
    def inrange(n, v):
        return v[0] <= int(n) <= v[1] or v[2] <= int(n) <= v[3]


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n\n")


def solution(data):
    """Solve part 1."""
    ticket = Ticket(data[0])
    yours = list(map(int, data[1].splitlines()[1].split(",")))
    cnt = 0
    valid = []
    for line in data[2].splitlines()[1:]:
        if ticket.invalid(line):
            cnt += ticket.invalid(line)
        else:
            valid.append(tuple(map(int, line.split(","))))
    cols = list(zip(*valid))
    info = []
    for i, col in enumerate(cols):
        info.append((i, ticket.fields(col)))
    info.sort(key=lambda x: x[1])
    f_info = []
    for i in range(len(info)):
        if i == 0:
            f_info.append(info[i])
        else:
            f_info.append((info[i][0], info[i][1] - info[i - 1][1]))
    res = []
    for k, names in f_info:
        for name in names:
            if name.startswith("departure"):
                res.append(yours[k])

    return cnt, math.prod(res)


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
