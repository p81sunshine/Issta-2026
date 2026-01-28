from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Failed for N=3, K=1"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Failed for N=4, K=11"

def test_mid_point_case():
    assert findKthBit(2, 2) == '1', "Failed for mid-point in N=2, K=2"

def test_base_case():
    assert findKthBit(1, 1) == '0', "Failed for base case N=1, K=1"

def test_another_mid_case():
    assert findKthBit(3, 4) == '1', "Failed for mid-point in N=3, K=4"