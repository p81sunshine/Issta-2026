from solution import *

def test_example_1():
    input = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(input) == expected, "Failed for first example"

def test_example_3():
    input = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(input) == expected, "Failed for third example"

def test_simple_eulerian_path():
    input = [[0,1],[1,2]]
    expected = [[0,1],[1,2]]
    assert validArrangement(input) == expected, "Failed for simple path"