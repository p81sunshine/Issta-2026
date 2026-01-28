from solution import *

def test_example_1():
    assert maxDistance([55,30,5,4,2], [100,20,10,10,5]) == 2, "Example 1 failed"

def test_example_2():
    assert maxDistance([2,2,2], [10,10,1]) == 1, "Example 2 failed"

def test_example_3():
    assert maxDistance([30,29,19,5], [25,25,25,25,25]) == 2, "Example 3 failed"

def test_case_all_same_length():
    assert maxDistance([1,2,3], [1,2,3]) == 2, "Test case for same arrays failed"

def test_case_single_element_in_nums1():
    assert maxDistance([1], [1,2,3]) == 2, "Test case for single element nums1 failed"