import pathlib
import pytest
import day16 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return puzzle_input

@pytest.mark.skip()
def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    ticket = aoc.Ticket(parsed_input[0])
    assert ticket.invalid('55,2,20') == 55
    assert aoc.solution(parsed_input) == 71


def test_part2(example2):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(example2)
    assert aoc.solution(parsed_input)[1] == 1716
