from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert valid_arrangement(pairs) == expected, "Failed for example 1"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert valid_arrangement(pairs) == expected, "Failed for example 3"

def test_simple_case():
    pairs = [[0,1],[1,2]]
    expected = [[0,1],[1,2]]
    assert valid_arrangement(pairs) == expected, "Failed for simple case"