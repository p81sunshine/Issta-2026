from solution import *

def test_example_1():
    assert findMinimumTime([[2,3,1],[4,5,1],[1,5,2]]) == 2

def test_example_2():
    assert findMinimumTime([[1,3,2],[2,5,3],[5,6,2]]) == 4

def test_single_task():
    assert findMinimumTime([[1,1,1]]) == 1, "Single task allocation failed"

def test_task_needs_two_units():
    assert findMinimumTime([[1,2,2]]) == 2, "Multi-unit task allocation failed"