from solution import *

def test_example_1():
    assert flipgame([1,2,4,4,7], [1,3,4,1,3]) == 2, "Example 1 should return 2"

def test_example_2():
    assert flipgame([1], [1]) == 0, "Example 2 should return 0"

def test_case_3():
    assert flipgame([2,3], [3,2]) == 2, "Test case where both sets are swapped"

def test_case_4():
    assert flipgame([2,3], [1,2]) == 1, "Test case with overlapping values in fronts and backs"

def test_edge_case():
    assert flipgame([1,2], [2,1]) == 1, "Edge case with minimal valid choice"