from solution import *

def test_example_1():
    assert count_points("B0B6G0R6R0R6G9") == 1, "Example 1 failed"

def test_example_2():
    assert count_points("B0R0G0R9R0B0G0") == 1, "Example 2 failed"

def test_example_3():
    assert count_points("G4") == 0, "Example 3 failed"

def test_rod_with_two_colors():
    assert count_points("R0G0") == 0, "Rod with two colors should return 0"

def test_rod_with_all_three_colors():
    assert count_points("R0G0B0") == 1, "Rod with all three colors should return 1"