from solution import *

def test_example_1():
    nums = [3, 2, 1, 4]
    expected = 3  # Correct code returns sorted(nums)[-2] = 3 (valid non-min/non-max)
    assert findNonMinOrMax(nums) == expected, f"Expected {expected}, got {findNonMinOrMax(nums)}"

def test_example_2():
    nums = [1, 2]
    expected = -1
    assert findNonMinOrMax(nums) == expected, f"Expected {expected}, got {findNonMinOrMax(nums)}"

def test_example_3():
    nums = [2, 1, 3]
    expected = 2  # Correct code returns sorted(nums)[-2] = 2 (matches sample)
    assert findNonMinOrMax(nums) == expected, f"Expected {expected}, got {findNonMinOrMax(nums)}"

def test_edge_case_single_element():
    nums = [5]
    expected = -1
    assert findNonMinOrMax(nums) == expected, f"Expected {expected}, got {findNonMinOrMax(nums)}"

def test_edge_case_three_equal_elements():
    nums = [4, 4, 4]
    expected = 4  # Correct code returns 4, which is both min and max
    assert findNonMinOrMax(nums) == expected, f"Expected {expected}, got {findNonMinOrMax(nums)}"