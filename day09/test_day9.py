import pathlib
import pytest
import day9 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_part(example):
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input, n=5) == 127
    assert aoc.part2(parsed_input, num=127) == 62
