import pathlib
import pytest
import day8 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input

def test_class(example):
    console = aoc.Console(example)
    assert console.acc == 0
    assert console.insts[0] == 'nop +0'
    console.run()
    assert console.acc == 5

def test_part2(example):
    """Test part 2 on example input."""
    assert aoc.part2(example) == 8
