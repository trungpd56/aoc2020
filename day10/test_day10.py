import pathlib
import pytest
import day10 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return puzzle_input


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("example", 35),
        ("example2", 220),
    ],
)
def test_part1(puzzle_input, expected, request):
    """Test part 1 on example input."""
    example = request.getfixturevalue(puzzle_input)
    parsed_input = aoc.parse(example)
    assert aoc.part1(parsed_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("example", 8),
        ("example2", 19208),
    ],
)
def test_part2(puzzle_input, expected, request):
    """Test part 2 on example input."""
    example = request.getfixturevalue(puzzle_input)
    parsed_input = aoc.parse(example)
    assert aoc.part2([0], parsed_input) == expected
