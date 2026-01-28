from solution import *

def test_example_1():
    assert maxPoints([[1,1],[2,2],[3,3]]) == 3, "Should return 3 for 3 collinear points"

def test_example_2():
    assert maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4, "Should return 4 for sample input with maximum 4 points"

def test_edge_case_single_point():
    assert maxPoints([[0,0]]) == 1, "Should return 1 for single point"

def test_edge_case_two_points():
    assert maxPoints([[0,0], [1,1]]) == 2, "Should return 2 for two points"

def test_edge_case_vertical_line():
    assert maxPoints([[0,0], [0,1], [0,2]]) == 3, "Should handle vertical line case correctly"