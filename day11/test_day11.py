import pathlib
import pytest
import day11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert parsed_input[0][1] == "."
    assert parsed_input[2][2] == "L"
    assert aoc.solution(parsed_input) == 37
    assert aoc.solution(parsed_input, p2=True) == 26


# def test_part2(example):
#     """Test part 2 on example input."""
#     parsed_input = aoc.parse(example)
#     assert aoc.part2(parsed_input) == 26
