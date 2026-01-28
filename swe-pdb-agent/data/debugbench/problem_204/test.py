from solution import *

def test_example_1():
    numCourses = 2
    prerequisites = [[1, 0]]
    assert can_finish(numCourses, prerequisites) is True, "Example 1 failed"

def test_example_2():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    assert can_finish(numCourses, prerequisites) is False, "Example 2 failed"

def test_cycle_with_multiple_paths():
    numCourses = 3
    prerequisites = [[0, 1], [1, 2], [2, 0], [0, 2]]
    assert can_finish(numCourses, prerequisites) is False, "Cycle with multiple paths failed"