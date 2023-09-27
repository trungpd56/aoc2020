import pathlib
import pytest
import day4 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return puzzle_input


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return puzzle_input


def test_valid1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert aoc.valid(parsed_input[0]) == True
    assert aoc.valid(parsed_input[1]) == False
    assert aoc.valid(parsed_input[2]) == True
    assert aoc.valid(parsed_input[3]) == False


def test_valid2(example2):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example2)
    assert aoc.valid(parsed_input[0], p2=True) == False
    assert aoc.valid(parsed_input[1], p2=True) == False
    assert aoc.valid(parsed_input[2], p2=True) == False
    assert aoc.valid(parsed_input[3], p2=True) == False


def test_valid3(example3):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example3)
    assert aoc.valid(parsed_input[0], p2=True) == True
    assert aoc.valid(parsed_input[1], p2=True) == True
    assert aoc.valid(parsed_input[2], p2=True) == True
    assert aoc.valid(parsed_input[3], p2=True) == True
