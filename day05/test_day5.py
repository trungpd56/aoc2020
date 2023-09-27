import pytest
import day5 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
        ("FBFBBFFRLR", 357),
    ],
)
def test_seat(puzzle_input, expected):
    """Test part 1 on example input."""
    assert aoc.seat(puzzle_input) == expected


