from solution import *

def test_example_1():
    assert minBitFlips(10, 7) == 3, "Example 1: start=10, goal=7 should return 3"

def test_example_2():
    assert minBitFlips(3, 4) == 3, "Example 2: start=3, goal=4 should return 3"

def test_same_value():
    assert minBitFlips(5, 5) == 0, "Edge case: same input and goal should return 0"

def test_max_flip_case():
    max_flips_value = (1 << 50) - 1  # 50 bits of 1s
    assert minBitFlips(0, max_flips_value) == 50, "Edge case: all 50 bits differ"

def test_single_bit_flip():
    assert minBitFlips(0, 1) == 1, "Single bit difference should return 1"