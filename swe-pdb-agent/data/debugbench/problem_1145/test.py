from solution import *

def test_example_1():
    assert minBitFlips(10, 7) == 3, "Example 1 failed"

def test_example_2():
    assert minBitFlips(3, 4) == 3, "Example 2 failed"

def test_edge_case_1():
    assert minBitFlips(0, 1 << 49) == 1, "Edge case with 50th bit mismatch failed"

def test_edge_case_2():
    assert minBitFlips(0, 0) == 0, "Edge case with identical values failed"

def test_edge_case_3():
    assert minBitFlips((1 << 50) - 1, 0) == 50, "Edge case with all bits set failed"