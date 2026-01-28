from solution import *

def test_example_1():
    nums = [1,3,2,2,5,2,3,7]
    assert find_lhs(nums) == 5, "Example 1 failed"

def test_example_2():
    nums = [1,2,3,4]
    assert find_lhs(nums) == 2, "Example 2 failed"

def test_example_3():
    nums = [1,1,1,1]
    assert find_lhs(nums) == 0, "Example 3 failed"

def test_additional_case():
    nums = [2,2,2,3,3]
    assert find_lhs(nums) == 5, "Additional case failed"