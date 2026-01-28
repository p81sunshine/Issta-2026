from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Example 1 failed"

def test_example_2():
    assert findComplement(1) == 0, "Example 2 failed"

def test_edge_case_1():
    assert findComplement(2) == 1, "Edge case with num=2 failed"