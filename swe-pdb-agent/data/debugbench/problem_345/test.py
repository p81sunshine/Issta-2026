from solution import *

def test_example_1():
    input_data = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(input_data) == expected, "Example 1 failed"

def test_example_3():
    input_data = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(input_data) == expected, "Example 3 failed"

def test_custom_case():
    input_data = [[1,2],[2,3],[3,1],[1,4]]
    expected = [[1,2],[2,3],[3,1],[1,4]]
    assert validArrangement(input_data) == expected, "Custom test case failed"