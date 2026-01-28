from solution import *

def test_example_1():
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    assert fourSumCount(nums1, nums2, nums3, nums4) == 2

def test_example_2():
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    assert fourSumCount(nums1, nums2, nums3, nums4) == 1

def test_duplicate_combinations():
    nums1 = [0, 0]
    nums2 = [0, 0]
    nums3 = [0]
    nums4 = [0]
    assert fourSumCount(nums1, nums2, nums3, nums4) == 4

def test_no_valid_quadruple():
    nums1 = [1]
    nums2 = [2]
    nums3 = [3]
    nums4 = [4]
    assert fourSumCount(nums1, nums2, nums3, nums4) == 0