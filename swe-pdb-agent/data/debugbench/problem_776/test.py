from solution import *

def test_example_1():
    assert validArrangement([[5,1],[4,5],[11,9],[9,4]]) == [[11,9],[9,4],[4,5],[5,1]], "Example 1 failed"

def test_example_2():
    result = validArrangement([[1,3],[3,2],[2,1]])
    expected = [[1,3],[3,2],[2,1]]
    assert result == expected or result == [[3,2],[2,1],[1,3]] or result == [[2,1],[1,3],[3,2]], "Example 2 failed"

def test_example_3():
    assert validArrangement([[1,2],[1,3],[2,1]]) == [[1,2],[2,1],[1,3]], "Example 3 failed"

def test_single_pair():
    assert validArrangement([[1,2]]) == [[1,2]], "Single pair test failed"