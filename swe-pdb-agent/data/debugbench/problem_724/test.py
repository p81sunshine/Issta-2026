from solution import *

def test_example_1():
    assert validArrangement([[5,1],[4,5],[11,9],[9,4]]) == [[11,9],[9,4],[4,5],[5,1]], "Example 1 failed"

def test_example_3():
    assert validArrangement([[1,2],[1,3],[2,1]]) == [[1,2],[2,1],[1,3]], "Example 3 failed"

def test_single_pair():
    assert validArrangement([[1,2]]) == [[1,2]], "Single pair test failed"