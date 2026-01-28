from solution import *

def test_example_1():
    assert max_points([[1,1],[2,2],[3,3]]) == 3, "Example 1 failed: all points on same line"

def test_example_2():
    assert max_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4, "Example 2 failed: max 4 points on a line"

def test_single_point():
    assert max_points([[0,0]]) == 1, "Single point edge case failed"

def test_two_points():
    assert max_points([[1,1],[2,3]]) == 2, "Two distinct points case failed"

def test_no_colinear():
    assert max_points([[0,0],[0,1],[1,0],[1,1],[2,3]]) == 2, "No colinear points case failed"