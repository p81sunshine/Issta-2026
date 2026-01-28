from solution import *

def test_example_1():
    assert min_flips(2, 6, 5) == 3, "Example 1 failed"

def test_example_2():
    assert min_flips(4, 2, 7) == 1, "Example 2 failed"

def test_example_3():
    assert min_flips(1, 2, 3) == 0, "Example 3 failed"

def test_edge_case_all_zeros():
    assert min_flips(0, 0, 0) == 0, "All zeros case failed"

def test_edge_case_c_has_1_but_none_in_a_or_b():
    assert min_flips(0, 0, 1) == 1, "c has 1 but a and b have 0"

def test_edge_case_c_has_0_but_both_a_and_b_have_1():
    assert min_flips(1, 1, 0) == 2, "c is 0, a and b are 1"