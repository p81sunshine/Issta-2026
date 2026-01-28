from solution import *

def test_example_1():
    assert minBitFlips(10, 7) == 3, "Example 1 failed"

def test_example_2():
    assert minBitFlips(3, 4) == 3, "Example 2 failed"

def test_same_values():
    assert minBitFlips(0, 0) == 0, "Same values should return 0"

def test_single_bit_diff():
    assert minBitFlips(1 << 49, 0) == 1, "Single bit difference at 50th position"

def test_all_bits_diff():
    assert minBitFlips((1 << 50) - 1, 0) == 50, "All 50 bits differ"