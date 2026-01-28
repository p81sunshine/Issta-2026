from solution import *

def test_example_1():
    nums = [2, 0, 2, 1, 1, 0]
    expected = [0, 0, 1, 1, 2, 2]
    sortColors(nums)
    assert nums == expected, f"Expected {expected}, but got {nums}"

def test_example_2():
    nums = [2, 0, 1]
    expected = [0, 1, 2]
    sortColors(nums)
    assert nums == expected, f"Expected {expected}, but got {nums}"

def test_mixed_swap_case():
    nums = [1, 2, 0]
    expected = [0, 1, 2]
    sortColors(nums)
    assert nums == expected, f"Expected {expected}, but got {nums}"

def test_multiple_twos_case():
    nums = [0, 2, 1, 2]
    expected = [0, 1, 2, 2]
    sortColors(nums)
    assert nums == expected, f"Expected {expected}, but got {nums}"

def test_all_twos():
    nums = [2, 2, 2]
    expected = [2, 2, 2]
    sortColors(nums)
    assert nums == expected, f"Expected {expected}, but got {nums}"