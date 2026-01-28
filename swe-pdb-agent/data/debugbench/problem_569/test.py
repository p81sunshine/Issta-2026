from solution import *

def test_example_1():
    n = 7
    cost = [1,5,2,2,3,3,1]
    assert minIncrements(n, cost) == 6, "Example 1 should return 6"

def test_example_2():
    n = 3
    cost = [5,3,3]
    assert minIncrements(n, cost) == 0, "Example 2 should return 0"

def test_single_node():
    n = 1
    cost = [0]
    assert minIncrements(n, cost) == 0, "Single node should return 0"

def test_case_n5():
    n = 5
    cost = [0, 1, 2, 3, 4]
    assert minIncrements(n, cost) == 4, "Test case n=5 should return 4"