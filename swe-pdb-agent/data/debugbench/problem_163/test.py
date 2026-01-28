from solution import *

def test_example_1():
    nums = [6,2,2,2,6]
    edges = [[0,1],[1,2],[1,3],[3,4]]
    assert componentValue(nums, edges) == 2, "Example 1 failed"

def test_example_2():
    nums = [2]
    edges = []
    assert componentValue(nums, edges) == 0, "Example 2 failed"

def test_case_3():
    nums = [3,3]
    edges = [[0,1]]
    assert componentValue(nums, edges) == 1, "Test case 3 failed"

def test_case_4():
    nums = [1,1,2]
    edges = [[0,1], [1,2]]
    assert componentValue(nums, edges) == 1, "Test case 4 failed"