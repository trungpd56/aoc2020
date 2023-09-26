import pathlib
import pytest
import day1 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input

def test_solution(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    # assert aoc.solution(parsed_input) == 514579
    assert aoc.solution(parsed_input, n=3) == 241861950

