from solution import *

def test_example_1():
    nums1 = [4,3,1,2]
    nums2 = [2,4,9,5]
    queries = [[4,1],[1,3],[2,5]]
    expected = [6,10,7]
    actual = maximumSumQueries(nums1, nums2, queries)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    nums1 = [3,2,5]
    nums2 = [2,3,4]
    queries = [[4,4],[3,2],[1,1]]
    expected = [9,9,9]
    actual = maximumSumQueries(nums1, nums2, queries)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_3():
    nums1 = [2,1]
    nums2 = [2,3]
    queries = [[3,3]]
    expected = [-1]
    actual = maximumSumQueries(nums1, nums2, queries)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_custom_case():
    nums1 = [1,2,3]
    nums2 = [1,3,2]
    queries = [[1,3]]
    expected = [5]
    actual = maximumSumQueries(nums1, nums2, queries)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_edge_case_n_1():
    nums1 = [5]
    nums2 = [5]
    queries = [[5,5]]
    expected = [10]
    actual = maximumSumQueries(nums1, nums2, queries)
    assert actual == expected, f"Expected {expected} but got {actual}"