from solution import *

def test_example_1():
    assert addNegabinary([1,1,1,1,1], [1,0,1]) == [1,0,0,0,0], "Failed for example 1"

def test_example_2():
    assert addNegabinary([0], [0]) == [0], "Failed for example 2"

def test_example_3():
    assert addNegabinary([0], [1]) == [1], "Failed for example 3"

def test_edge_case_zero_sum():
    # 1 + (-1) = 0 in decimal
    # 1 in negabinary is [1], -1 in negabinary is [1,1]
    assert addNegabinary([1], [1,1]) == [0], "Failed for zero sum edge case"