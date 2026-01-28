from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Example 1 failed"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Example 2 failed"

def test_k_in_right_section():
    assert findKthBit(3, 5) == '0', "Failed for N=3, K=5 (right section handling)"

def test_mid_position():
    assert findKthBit(2, 2) == '1', "Failed for N=2, K=2 (mid position handling)"

def test_edge_k_equals_mid():
    assert findKthBit(3, 4) == '1', "Failed for N=3, K=4 (midpoint case)"