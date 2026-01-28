from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Failed for n=3, k=1"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Failed for n=4, k=11"

def test_mid_value_n2_k2():
    assert findKthBit(2, 2) == '1', "Failed for n=2, k=2"

def test_mid_value_n3_k4():
    assert findKthBit(3, 4) == '1', "Failed for n=3, k=4"

def test_edge_case_n1_k1():
    assert findKthBit(1, 1) == '0', "Failed for n=1, k=1"