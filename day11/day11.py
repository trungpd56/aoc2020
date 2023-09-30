#!/usr/bin/env python3

import pathlib
import sys
from rich import print


def parse(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def cnt_seats(r: int, c: int, data: list, p2: bool = False) -> int:
    maxr = len(data)
    maxc = len(data[0])
    adjs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    if not p2:
        nseats = [
            data[r + dr][c + dc]
            for dr, dc in adjs
            if 0 <= r + dr < maxr and 0 <= c + dc < maxc
        ]
        cnt = nseats.count("#")
        return cnt
    total = 0
    for dr, dc in adjs:
        cnt = 0
        rr, cc = r+dr , c+dc
        while 0 <= rr < maxr and 0 <= cc < maxc:
            match data[rr][cc]:
                case "L":
                    cnt = 0
                    break
                case "#":
                    cnt += 1
                    break
                case _:
                    rr += dr
                    cc += dc
        total += cnt
    return total


def solution(data, p2=False):
    """Solve part 1."""
    maxr = len(data)
    maxc = len(data[0])
    ncondition = 4 if not p2 else 5
    while True:
        ndata = [["" for _ in range(maxc)] for _ in range(maxr)]
        changed = False
        for r in range(maxr):
            for c in range(maxc):
                cnt = cnt_seats(r, c, data, p2)
                if data[r][c] == "L" and cnt == 0:
                    ndata[r][c] = "#"
                    changed = True
                elif data[r][c] == "#" and cnt >= ncondition:
                    ndata[r][c] = "L"
                    changed = True
                else:
                    ndata[r][c] = data[r][c]
        if not changed:
            return [c for r in ndata for c in r].count("#")
        data = ndata



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = solution(data)
    solution2 = solution(data, p2=True)

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
