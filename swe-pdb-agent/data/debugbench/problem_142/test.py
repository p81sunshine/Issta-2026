from solution import *

def test_example_1():
    nums = [1,1,1,2,2,3]
    expected_nums = [1,1,2,2,3]
    expected_k = 5
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k {expected_k}, but got {k}"
    assert nums[:k] == expected_nums, f"Expected nums[:{k}] {expected_nums}, but got {nums[:k]}"

def test_example_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_nums = [0,0,1,1,2,3,3]
    expected_k = 7
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k {expected_k}, but got {k}"
    assert nums[:k] == expected_nums, f"Expected nums[:{k}] {expected_nums}, but got {nums[:k]}"

def test_case_buggy_condition():
    nums = [1,1,2,2,2,3]
    expected_nums = [1,1,2,2,3]
    expected_k = 5
    k = removeDuplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_nums

def test_case_all_duplicates():
    nums = [1,1,1,1]
    expected_nums = [1,1]
    expected_k = 2
    k = removeDuplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_nums