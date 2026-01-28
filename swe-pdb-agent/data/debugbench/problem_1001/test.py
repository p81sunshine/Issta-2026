from solution import *

def test_example_1():
    assert max_points([[1,1],[2,2],[3,3]]) == 3, "All collinear points should return length 3"

def test_example_2():
    input_points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    assert max_points(input_points) == 4, "Sample input should return maximum 4 points"

def test_single_point():
    assert max_points([[0,0]]) == 1, "Single point should return 1"

def test_two_points():
    assert max_points([[2,3], [5,7]]) == 2, "Two points always form a line"

def test_vertical_line():
    points = [[1,2], [1,5], [1,-3], [1,0]]
    assert max_points(points) == 4, "All points on vertical line x=1"

def test_horizontal_line():
    points = [[-2,3], [5,3], [0,3], [3,3]]
    assert max_points(points) == 4, "All points on horizontal line y=3"