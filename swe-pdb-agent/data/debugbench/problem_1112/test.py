from solution import *

def test_example_1():
    assert isWinner([4,10,7,9], [6,5,2,3]) == 1, "Example 1 failed"

def test_example_2():
    assert isWinner([3,5,7,6], [8,10,10,2]) == 2, "Example 2 failed"

def test_example_3():
    assert isWinner([2,3], [4,1]) == 0, "Example 3 failed"

def test_edge_case_1():
    assert isWinner([10,5], [10,5]) == 0, "Edge case with [10,5] failed"

def test_edge_case_2():
    assert isWinner([5,10,3], [5,3,10]) == 1, "Edge case with [5,10,3] vs [5,3,10] failed"