import pathlib
import pytest
import day14 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return puzzle_input

def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input) == 165


def test_genadd():
    assert aoc.genadd('000000000000000000000000000000X1101X') == [26, 27, 58, 59]


def test_part2(example2):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(example2)
    assert aoc.part2(parsed_input) == 208
