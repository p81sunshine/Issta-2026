from solution import *

def test_example_1():
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    expected = 2
    actual = four_sum_count(nums1, nums2, nums3, nums4)
    assert actual == expected, "Example 1 failed"

def test_example_2():
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    expected = 1
    actual = four_sum_count(nums1, nums2, nums3, nums4)
    assert actual == expected, "Example 2 failed"

def test_case_3():
    nums1 = [1, -1]
    nums2 = [2, -2]
    nums3 = [1, -1]
    nums4 = [2, -2]
    expected = 4
    actual = four_sum_count(nums1, nums2, nums3, nums4)
    assert actual == expected, "Test case 3 failed"

def test_case_4():
    nums1 = [0, 0]
    nums2 = [0, 0]
    nums3 = [0]
    nums4 = [0]
    expected = 4
    actual = four_sum_count(nums1, nums2, nums3, nums4)
    assert actual == expected, "Test case 4 failed"