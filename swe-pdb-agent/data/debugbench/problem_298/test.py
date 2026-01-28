from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Example 1 failed"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Example 2 failed"

def test_mid_case():
    assert findKthBit(2, 2) == '1', "Mid position test failed"

def test_k_greater_than_mid():
    assert findKthBit(3, 5) == '0', "K > mid handling test failed"

def test_edge_n1():
    assert findKthBit(1, 1) == '0', "Edge case N=1, K=1 failed"