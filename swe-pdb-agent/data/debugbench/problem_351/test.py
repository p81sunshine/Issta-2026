from solution import *

def test_example_1():
    assert maxPoints([[1,1],[2,2],[3,3]]) == 3, "Example 1 failed"

def test_example_2():
    assert maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4, "Example 2 failed"

def test_edge_case_n1():
    assert maxPoints([[5,5]]) == 1, "Edge case N=1 failed"

def test_edge_case_n2():
    assert maxPoints([[0,0], [1,1]]) == 2, "Edge case N=2 failed"

def test_edge_case_vertical_lines():
    assert maxPoints([[0,0], [0,1], [0,2]]) == 3, "Vertical line case failed"