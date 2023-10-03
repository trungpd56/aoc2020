import pytest
import day15 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("0,3,6", 436),
        ("1,3,2", 1),
        ("2,1,3", 10),
        ("1,2,3", 27),
        ("2,3,1", 78),
        ("3,2,1", 438),
        ("3,1,2", 1836),
    ],
)
def test_solution(puzzle_input, expected):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.solution(parsed_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("0,3,6", 175594),
        ("1,3,2", 2578),
        ("2,1,3", 3544142),
        ("1,2,3", 261214),
        ("2,3,1", 6895259),
        ("3,2,1", 18),
        ("3,1,2", 362),
    ],
)
def test_solution2(puzzle_input, expected):
    """Test part 2 on example input."""
    parsed_input = aoc.parse(puzzle_input)
    assert aoc.solution(parsed_input, 30000000) == expected
