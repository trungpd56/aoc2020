import pathlib
import pytest
import day13 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return puzzle_input


def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert parsed_input[0] == 939
    assert parsed_input[1] == [7, 13, "x", "x", 59, "x", 31, 19]
    assert aoc.part1(parsed_input) == 295


def test_rem():
    assert aoc.chinese_remainder([5,7,8],[3,1,6]) == 78


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("17,x,13,19", 3417),
        ("67,7,59,61", 754018),
        ("67,x,7,59,61", 779210),
        ("67,7,x,59,61", 1261476),
        ("1789,37,47,1889", 1202161486),
    ],
)
def test_part2(puzzle_input, expected):
    """Test part 2 on example input."""
    assert aoc.part2(puzzle_input) == expected
