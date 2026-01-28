from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Example 1 failed: S3's 1st bit should be '0'"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Example 2 failed: S4's 11th bit should be '1'"

def test_case_n2_k3():
    assert findKthBit(2, 3) == '1', "N=2, K=3 should return '1' but would crash buggy code"

def test_case_n3_k5():
    assert findKthBit(3, 5) == '0', "N=3, K=5 should return '0' but would crash buggy code"

def test_edge_case_n1_k1():
    assert findKthBit(1, 1) == '0', "Edge case N=1, K=1 should return '0'"