from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Example 1 should return '0' for n=3, k=1"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Example 2 should return '1' for n=4, k=11"

def test_mid_case_1():
    assert findKthBit(2, 2) == '1', "Mid position for n=2, k=2 should return '1'"

def test_mid_case_2():
    assert findKthBit(3, 4) == '1', "Mid position for n=3, k=4 should return '1'"

def test_mid_case_3():
    assert findKthBit(4, 8) == '1', "Mid position for n=4, k=8 should return '1'"