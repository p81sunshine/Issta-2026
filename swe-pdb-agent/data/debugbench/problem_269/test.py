from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(pairs) == expected, "Failed for example 1"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(pairs) == expected, "Failed for example 3"

def test_single_edge():
    pairs = [[1,2]]
    expected = [[1,2]]
    assert validArrangement(pairs) == expected, "Failed for single edge case"