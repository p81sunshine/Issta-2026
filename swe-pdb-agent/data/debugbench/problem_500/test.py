from solution import *

def test_example_1():
    assert reverseBits(43261596) == 964176192, "First example failed"

def test_example_2():
    assert reverseBits(4294967293) == 3221225471, "Second example failed"

def test_zero_input():
    assert reverseBits(0) == 0, "Zero input should return zero"

def test_single_bit():
    assert reverseBits(1) == (1 << 31), "Single bit reversal failed"

def test_all_ones():
    assert reverseBits(0xFFFFFFFF) == 0xFFFFFFFF, "All ones should remain all ones after reversal"