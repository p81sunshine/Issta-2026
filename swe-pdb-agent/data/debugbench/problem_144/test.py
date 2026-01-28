from solution import *

def test_example_1():
    assert minimumDifference([90], 1) == 0, "Failed for single-element input"

def test_example_2():
    assert minimumDifference([9,4,1,7], 2) == 2, "Failed for standard example case"

def test_edge_case_full_array():
    assert minimumDifference([3,1,5], 3) == 4, "Failed when k equals array length"

def test_two_elements():
    assert minimumDifference([1, 2], 2) == 1, "Failed for two-element input"