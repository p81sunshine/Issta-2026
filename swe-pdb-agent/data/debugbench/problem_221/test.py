from solution import *

def test_example_1():
    n = 7
    cost = [1,5,2,2,3,3,1]
    assert minIncrements(n, cost) == 6, "Example 1 failed"

def test_example_2():
    n = 3
    cost = [5,3,3]
    assert minIncrements(n, cost) == 0, "Example 2 failed"

def test_single_node():
    n = 1
    cost = [10]
    assert minIncrements(n, cost) == 0, "Single node case failed"

def test_synthetic_case():
    n = 3
    cost = [1, 0, 2]
    assert minIncrements(n, cost) == 2, "Synthetic case failed"