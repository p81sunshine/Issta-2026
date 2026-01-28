from solution import *

def test_example_1():
    input_pairs = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert valid_arrangement(input_pairs) == expected, "Example 1 failed"

def test_example_3():
    input_pairs = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert valid_arrangement(input_pairs) == expected, "Example 3 failed"

def test_single_edge():
    input_pairs = [[1,2]]
    expected = [[1,2]]
    assert valid_arrangement(input_pairs) == expected, "Single edge case failed"