from solution import *

def test_example_1():
    nums = [1,1,1,2,2,3]
    expected_k = 5
    expected_nums = [1,1,2,2,3]
    k = remove_duplicates(nums)
    assert k == expected_k, f"Expected k {expected_k}, got {k}"
    for i in range(k):
        assert nums[i] == expected_nums[i], f"Value mismatch at index {i}: {nums[i]} vs {expected_nums[i]}"

def test_example_2():
    nums = [0,0,1,1,1,1,2,3,3]
    expected_k = 7
    expected_nums = [0,0,1,1,2,3,3]
    k = remove_duplicates(nums)
    assert k == expected_k, f"Expected k {expected_k}, got {k}"
    for i in range(k):
        assert nums[i] == expected_nums[i], f"Value mismatch at index {i}: {nums[i]} vs {expected_nums[i]}"

def test_bug_case():
    nums = [1,2,2,2,3]
    expected_k = 4
    expected_nums = [1,2,2,3]
    k = remove_duplicates(nums)
    assert k == expected_k, "Buggy code would return incorrect k=5 here"
    for i in range(k):
        assert nums[i] == expected_nums[i], f"Value mismatch at index {i}: {nums[i]} vs {expected_nums[i]}"

def test_all_duplicates():
    nums = [2,2,2,2,2]
    expected_k = 2
    expected_nums = [2,2]
    k = remove_duplicates(nums)
    assert k == expected_k, "Buggy code would return incorrect k=3 here"
    for i in range(k):
        assert nums[i] == expected_nums[i], f"Value mismatch at index {i}: {nums[i]} vs {expected_nums[i]}"

def test_less_than_three():
    nums = [1,1]
    expected_k = 2
    expected_nums = [1,1]
    k = remove_duplicates(nums)
    assert k == expected_k, "Edge case with 2 elements failed"
    for i in range(k):
        assert nums[i] == expected_nums[i], f"Value mismatch at index {i}: {nums[i]} vs {expected_nums[i]}"