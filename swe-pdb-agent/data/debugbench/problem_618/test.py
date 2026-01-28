from solution import *

def test_example_1():
    assert maxPoints([[1,1],[2,2],[3,3]]) == 3, "Example 1 failed"

def test_example_2():
    assert maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4, "Example 2 failed"

def test_case_n_2():
    assert maxPoints([[1,1],[2,2]]) == 2, "N=2 case failed"

def test_case_n_1():
    assert maxPoints([[5,5]]) == 1, "N=1 case failed"

def test_vertical_line():
    assert maxPoints([[2,3],[2,5],[2,1],[2,4]]) == 4, "Vertical line case failed"