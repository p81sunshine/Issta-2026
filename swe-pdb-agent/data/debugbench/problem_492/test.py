from solution import *

def test_example_1():
    assert find_lhs([1,3,2,2,5,2,3,7]) == 5, "Example 1 should return 5"

def test_example_2():
    assert find_lhs([1,2,3,4]) == 2, "Example 2 should return 2"

def test_example_3():
    assert find_lhs([1,1,1,1]) == 0, "Example 3 should return 0"

def test_buggy_count_case():
    assert find_lhs([2,2,3,3,3]) == 5, "Should return 5 for [2,2,3,3,3]"

def test_another_buggy_case():
    assert find_lhs([5,5,5,6,6]) == 5, "Should return 5 for [5,5,5,6,6]"