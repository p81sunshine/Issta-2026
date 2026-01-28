from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Example 1 failed"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Example 2 failed"

def test_midpoint_n2():
    assert findKthBit(2, 2) == '1', "Midpoint case for N=2 failed"

def test_midpoint_n3():
    assert findKthBit(3, 4) == '1', "Midpoint case for N=3 failed"

def test_edge_case_n1():
    assert findKthBit(1, 1) == '0', "Edge case N=1 failed"

def test_k_greater_than_mid_n3():
    assert findKthBit(3, 5) == '0', "K greater than mid in N=3 failed"