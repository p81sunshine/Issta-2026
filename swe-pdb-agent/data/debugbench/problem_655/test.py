from solution import *

def test_example_1():
    input = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(input) == expected, "Example 1 failed"

def test_example_3():
    input = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(input) == expected, "Example 3 failed"

def test_simple_path():
    input = [[1,2],[2,3]]
    expected = [[1,2],[2,3]]
    assert validArrangement(input) == expected, "Simple path test failed"