from solution import *

def test_example_1():
    assert can_finish(2, [[1, 0]]) == True, "Example 1 should return True"

def test_example_2():
    assert can_finish(2, [[1, 0], [0, 1]]) == False, "Example 2 should return False"

def test_cycle_with_three_courses():
    assert can_finish(3, [[1, 0], [2, 1], [0, 2]]) == False, "Cycle of three courses should return False"

def test_no_prerequisites():
    assert can_finish(3, []) == True, "No prerequisites should return True"

def test_multiple_paths():
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True, "Multiple valid paths should return True"