from solution import *

def test_example_1():
    # Input: stones = [7,4,9]
    assert numMovesStonesII([7,4,9]) == [1,2], "Example 1 failed"

def test_example_2():
    # Input: stones = [6,5,4,3,10]
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Example 2 failed"

def test_edge_case_indexing_bug():
    # Test case designed to trigger indexing error in buggy code
    assert numMovesStonesII([1, 3, 5, 8]) == [2, 3], "Edge case for indexing bug failed"