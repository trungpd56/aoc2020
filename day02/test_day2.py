import pathlib
import pytest
import day2 as aoc


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("1-3 a: abcde", True),
        ("1-3 b: cdefg", False),
        ("2-9 c: ccccccccc", True),
    ],
)
def test_valid(puzzle_input, expected):
    assert aoc.is_valid(puzzle_input) == expected


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("1-3 a: abcde", True),
        ("1-3 b: cdefg", False),
        ("2-9 c: ccccccccc", False),
    ],
)
def test_valid2(puzzle_input, expected):
    assert aoc.is_valid(puzzle_input, p2=True) == expected
