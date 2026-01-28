from solution import *

def test_example_1():
    assert canFinish(2, [[1,0]]) is True, "Example 1 failed"

def test_example_2():
    assert canFinish(2, [[1,0],[0,1]]) is False, "Example 2 failed"

def test_single_course_no_prereq():
    assert canFinish(1, []) is True, "Single course with no prerequisites should return True"

def test_chain_of_prerequisites():
    prerequisites = [[1,0], [2,1], [3,2]]
    assert canFinish(4, prerequisites) is True, "Linear chain of prerequisites should be possible"

def test_cycle_with_self_reference():
    assert canFinish(1, [[0,0]]) is False, "Self-referential cycle should return False"