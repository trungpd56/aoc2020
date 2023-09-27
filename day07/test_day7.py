import pathlib
import pytest
import day7 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
   puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
   return puzzle_input

def test_part1(example):
    """Test part 1 on example input."""
    parsed_input = aoc.parse(example)
    assert parsed_input['bright white']['shiny gold'] == 1
    assert aoc.valid('bright white', 'shiny gold', parsed_input) == True
    assert aoc.valid('dark orange', 'shiny gold', parsed_input) == True
    assert aoc.valid('faded blue', 'shiny gold', parsed_input) == False
    assert aoc.part1(parsed_input) == 4
    assert aoc.cnt_bags('shiny gold', parsed_input) == 32


