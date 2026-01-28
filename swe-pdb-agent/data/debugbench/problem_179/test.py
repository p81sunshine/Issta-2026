from solution import *

def test_example_1():
    nums = [1,1,1,2,2,3]
    expected_k = 5
    expected_nums = [1,1,2,2,3]
    copied_nums = nums.copy()
    k = removeDuplicates(copied_nums)
    assert k == expected_k, f"Expected k {expected_k}, got {k}"
    assert copied_nums[:k] == expected_nums, f"Expected nums {expected_nums}, got {copied_nums[:k]}"

def test_example_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_k = 7
    expected_nums = [0,0,1,1,2,3,3]
    copied_nums = nums.copy()
    k = removeDuplicates(copied_nums)
    assert k == expected_k
    assert copied_nums[:k] == expected_nums

def test_case_3():
    nums = [1,1,2,2]
    expected_k = 4
    expected_nums = [1,1,2,2]
    copied_nums = nums.copy()
    k = removeDuplicates(copied_nums)
    assert k == expected_k
    assert copied_nums[:k] == expected_nums

def test_case_4():
    nums = [2,2,3,3,3]
    expected_k = 4
    expected_nums = [2,2,3,3]
    copied_nums = nums.copy()
    k = removeDuplicates(copied_nums)
    assert k == expected_k
    assert copied_nums[:k] == expected_nums

def test_case_5():
    nums = [1,1,2,2,2]
    expected_k = 4
    expected_nums = [1,1,2,2]
    copied_nums = nums.copy()
    k = removeDuplicates(copied_nums)
    assert k == expected_k
    assert copied_nums[:k] == expected_nums