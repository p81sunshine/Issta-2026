from solution import *

def test_example_1():
    nums = [1,1,1,2,2,3]
    expected_k = 5
    expected_nums = [1,1,2,2,3]
    copied = nums.copy()
    actual_k = removeDuplicates(copied)
    assert actual_k == expected_k, f"Expected k={expected_k}, got {actual_k}"
    assert copied[:actual_k] == expected_nums, f"Expected nums[:k]={expected_nums}, got {copied[:actual_k]}"

def test_example_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_k = 7
    expected_nums = [0,0,1,1,2,3,3]
    copied = nums.copy()
    actual_k = removeDuplicates(copied)
    assert actual_k == expected_k, f"Expected k={expected_k}, got {actual_k}"
    assert copied[:actual_k] == expected_nums, f"Expected nums[:k]={expected_nums}, got {copied[:actual_k]}"

def test_case_len_2_same():
    nums = [1,1]
    expected_k = 2
    expected_nums = [1,1]
    copied = nums.copy()
    actual_k = removeDuplicates(copied)
    assert actual_k == expected_k, f"Expected k={expected_k}, got {actual_k}"
    assert copied[:actual_k] == expected_nums, f"Expected nums[:k]={expected_nums}, got {copied[:actual_k]}"

def test_case_len_2_diff():
    nums = [1,2]
    expected_k = 2
    expected_nums = [1,2]
    copied = nums.copy()
    actual_k = removeDuplicates(copied)
    assert actual_k == expected_k, f"Expected k={expected_k}, got {actual_k}"
    assert copied[:actual_k] == expected_nums, f"Expected nums[:k]={expected_nums}, got {copied[:actual_k]}"

def test_case_len_3_same():
    nums = [1,1,1]
    expected_k = 2
    expected_nums = [1,1]
    copied = nums.copy()
    actual_k = removeDuplicates(copied)
    assert actual_k == expected_k, f"Expected k={expected_k}, got {actual_k}"
    assert copied[:actual_k] == expected_nums, f"Expected nums[:k]={expected_nums}, got {copied[:actual_k]}"