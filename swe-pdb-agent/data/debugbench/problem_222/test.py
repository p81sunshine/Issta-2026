from solution import *

def test_case_single_element():
    assert minimumDifference([90], 1) == 0, "Failed for single element case"

def test_case_example_2():
    assert minimumDifference([9,4,1,7], 2) == 2, "Failed for example 2"

def test_case_k_equals_length():
    assert minimumDifference([3,1,2], 3) == 2, "Failed when k equals array length"

def test_case_small_window():
    assert minimumDifference([1,2,3], 2) == 1, "Failed for small window case"

def test_case_two_elements():
    assert minimumDifference([5,3], 2) == 2, "Failed for two elements case"