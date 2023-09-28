#!/usr/bin/env python3

import pathlib
import sys


class Console:
    def __init__(self, puzzle_input):
        self.acc = 0
        self.insts = puzzle_input.splitlines()
        self.eip = 0
        self.done = set()

    def run(self):
        while self.eip not in self.done:
            self.done.add(self.eip)
            cmd, value = self.insts[self.eip].split()
            value = int(value)
            match cmd:
                case "nop":
                    self.eip += 1
                case "acc":
                    self.acc += value
                    self.eip += 1
                case "jmp":
                    self.eip += value
            if self.eip == len(self.insts):
                return True
        return False


def part2(puzzle_input):
    """Solve part 2."""
    lines = puzzle_input.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("nop"):
            line = line.replace("nop", "jmp")
        elif line.startswith("jmp"):
            line = line.replace("jmp", "nop")
        else:
            continue
        temp = lines[:i] + [line] + lines[i + 1 :]
        console = Console("\n".join(temp))
        if console.run():
            return console.acc


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    console = Console(puzzle_input)
    console.run()
    solution1 = console.acc
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
