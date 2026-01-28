from solution import *

def test_example_1():
    assert minimumOperations([1,5,0,3,5]) == 3, "Example 1 failed"

def test_example_2():
    assert minimumOperations([0]) == 0, "Example 2 failed"

def test_all_non_zero():
    assert minimumOperations([1,2,3]) == 3, "All non-zero test failed"

def test_duplicates_non_zero():
    assert minimumOperations([2,2,2]) == 1, "Duplicates test failed"

def test_multiple_zeros():
    assert minimumOperations([0,0,1,0,2]) == 2, "Multiple zeros test failed"