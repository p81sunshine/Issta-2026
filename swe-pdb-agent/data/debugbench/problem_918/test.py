from solution import *

def test_example_1():
    assert minimumDifference([90], 1) == 0, "Failed for single-element case"

def test_example_2():
    assert minimumDifference([9,4,1,7], 2) == 2, "Failed for sample input case"

def test_window_size_match():
    assert minimumDifference([1,2,3,4], 2) == 1, "Failed for adjacent elements case"

def test_larger_window_case():
    assert minimumDifference([1,3,5,7], 3) == 4, "Failed for 3-element window case"

def test_full_length_window():
    assert minimumDifference([5,1,3], 3) == 4, "Failed when k equals array length"