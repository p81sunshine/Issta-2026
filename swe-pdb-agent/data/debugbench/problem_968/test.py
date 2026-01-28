from solution import *

def test_example_1():
    assert nthUglyNumber(3, 2, 3, 5) == 4, "Example 1 failed"

def test_example_2():
    assert nthUglyNumber(4, 2, 3, 4) == 6, "Example 2 failed"

def test_example_3():
    assert nthUglyNumber(5, 2, 11, 13) == 10, "Example 3 failed"

def test_edge_n1():
    assert nthUglyNumber(1, 3, 5, 2) == 2, "Edge case n=1 failed"

def test_duplicate_params():
    assert nthUglyNumber(5, 2, 2, 2) == 10, "Duplicate parameters test failed"