from solution import *

def test_example_1():
    nums = [1,1,1,2,2,3]
    expected_k = 5
    expected_nums = [1,1,2,2,3]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"Expected nums[:{k}]={expected_nums}, got {nums[:k]}"

def test_example_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_k = 7
    expected_nums = [0,0,1,1,2,3,3]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"Expected nums[:{k}]={expected_nums}, got {nums[:k]}"

def test_edge_case_1():
    nums = [1,1,1]
    expected_k = 2
    expected_nums = [1,1]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"Expected nums[:{k}]={expected_nums}, got {nums[:k]}"

def test_case_multiple_duplicates():
    nums = [1,1,2,2,3,3,3]
    expected_k = 6
    expected_nums = [1,1,2,2,3,3]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k={expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"Expected nums[:{k}]={expected_nums}, got {nums[:k]}"