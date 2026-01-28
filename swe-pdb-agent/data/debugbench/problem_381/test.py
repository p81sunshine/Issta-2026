from solution import *

def test_example_1():
    assert findKthNumber(13, 2) == 10, "Example 1 failed"

def test_example_2():
    assert findKthNumber(1, 1) == 1, "Example 2 failed"

def test_edge_case_1():
    assert findKthNumber(2, 1) == 1, "Edge case 1 failed"

def test_edge_case_2():
    assert findKthNumber(3, 3) == 3, "Edge case 2 failed"

def test_edge_case_3():
    assert findKthNumber(2, 2) == 2, "Edge case 3 failed"