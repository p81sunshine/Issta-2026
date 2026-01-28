from solution import *

def test_example_1():
    assert find_kth_number(13, 2) == 10, "Example 1 failed: n=13, k=2"

def test_example_2():
    assert find_kth_number(1, 1) == 1, "Example 2 failed: n=1, k=1"

def test_medium_case():
    assert find_kth_number(12, 5) == 2, "Test case n=12, k=5 failed"

def test_edge_case_k_equals_n():
    assert find_kth_number(10, 10) == 9, "Edge case: k equals sequence length"

def test_triple_digit_prefix():
    assert find_kth_number(100, 3) == 100, "Test case n=100, k=3 failed"