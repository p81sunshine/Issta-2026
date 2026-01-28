from solution import *

def test_example_1():
    nums = [1,1,1,2,2,3]
    expected_k = 5
    expected_nums = [1,1,2,2,3]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k = {expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"First {k} elements should be {expected_nums}, got {nums[:k]}"

def test_example_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_k = 7
    expected_nums = [0,0,1,1,2,3,3]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k = {expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"First {k} elements should be {expected_nums}, got {nums[:k]}"

def test_empty_list():
    nums = []
    expected_k = 0
    expected_nums = []
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k = {expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"First {k} elements should be {expected_nums}, got {nums[:k]}"

def test_all_unique():
    nums = [1,2,3,4]
    expected_k = 4
    expected_nums = [1,2,3,4]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k = {expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"First {k} elements should be {expected_nums}, got {nums[:k]}"

def test_multiple_duplicates():
    nums = [1,1,1,1]
    expected_k = 2
    expected_nums = [1,1]
    k = removeDuplicates(nums)
    assert k == expected_k, f"Expected k = {expected_k}, got {k}"
    assert nums[:k] == expected_nums, f"First {k} elements should be {expected_nums}, got {nums[:k]}"