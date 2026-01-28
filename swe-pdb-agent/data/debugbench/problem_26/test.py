from solution import *

def test_example_1():
    assert minimumDifference([90], 1) == 0, "Example 1 failed"

def test_example_2():
    assert minimumDifference([9,4,1,7], 2) == 2, "Example 2 failed"

def test_k_equals_1():
    assert minimumDifference([5, 10, 15], 1) == 0, "k=1 edge case failed"

def test_multiple_windows():
    assert minimumDifference([1,2,3,4,5], 3) == 2, "Multiple windows case failed"

def test_all_same_elements():
    assert minimumDifference([5,5,5], 2) == 0, "All elements same case failed"