from solution import *

def test_example_1():
    grid = [[1,1,1],[1,0,0],[1,1,1]]
    assert is_possible_to_cut_path(grid) is True, "Example 1 failed"

def test_example_2():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    assert is_possible_to_cut_path(grid) is False, "Example 2 failed"

def test_straight_vertical_path():
    grid = [[1], [1], [1]]
    assert is_possible_to_cut_path(grid) is True, "Straight vertical path test failed"

def test_single_cell():
    grid = [[1]]
    assert is_possible_to_cut_path(grid) is False, "Single cell test failed"

def test_2x2_full_path():
    grid = [[1,1], [1,1]]
    assert is_possible_to_cut_path(grid) is False, "2x2 full path test failed"