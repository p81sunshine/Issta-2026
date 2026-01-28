from solution import *

def test_example_1():
    assert numberOfArrays("1000", 10000) == 1, "Example 1 failed"

def test_example_2():
    assert numberOfArrays("1000", 10) == 0, "Example 2 failed"

def test_example_3():
    assert numberOfArrays("1317", 2000) == 8, "Example 3 failed"

def test_case_12_20():
    assert numberOfArrays("12", 20) == 2, "Test case '12' with k=20 failed"

def test_edge_case_0():
    assert numberOfArrays("0", 1) == 0, "Edge case '0' failed"

def test_edge_case_1():
    assert numberOfArrays("1", 1) == 1, "Edge case '1' failed"