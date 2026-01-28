from solution import *

def test_example_1():
    assert minBitFlips(10, 7) == 3, "Example 1 failed"

def test_example_2():
    assert minBitFlips(3, 4) == 3, "Example 2 failed"

def test_edge_zero():
    assert minBitFlips(0, 0) == 0, "Edge case with zero inputs failed"

def test_all_bits_diff():
    assert minBitFlips(0, (1 << 50) - 1) == 50, "All bits different test failed"

def test_single_flip():
    assert minBitFlips(1, 0) == 1, "Single bit flip test failed"