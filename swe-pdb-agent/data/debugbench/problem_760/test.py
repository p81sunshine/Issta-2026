from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Example 1: 5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Example 2: 1 should return 0"

def test_edge_case_1():
    assert findComplement(3) == 0, "Edge case: 3 should return 0"

def test_edge_case_2():
    assert findComplement(2) == 1, "Edge case: 2 should return 1"