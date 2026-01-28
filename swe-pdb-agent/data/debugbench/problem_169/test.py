from solution import *

def test_example_1():
    assert convertToTitle(1) == "A", "Example 1 failed: Input 1 should return 'A'"

def test_example_2():
    assert convertToTitle(28) == "AB", "Example 2 failed: Input 28 should return 'AB'"

def test_example_3():
    assert convertToTitle(701) == "ZY", "Example 3 failed: Input 701 should return 'ZY'"

def test_edge_case_1():
    assert convertToTitle(27) == "AA", "Edge case failed: Input 27 should return 'AA'"