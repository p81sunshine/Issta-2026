from solution import *

def test_example_1():
    nums = [1,2,4,6]
    operations = [[1,3],[4,7],[6,1]]
    expected = [3,2,7,1]
    assert arrayChange(nums, operations) == expected, "Example 1 failed"

def test_example_2():
    nums = [1,2]
    operations = [[1,3],[2,1],[3,2]]
    expected = [2,1]
    assert arrayChange(nums, operations) == expected, "Example 2 failed"

def test_chained_replacement():
    nums = [5,3]
    operations = [[5,3], [3,5]]
    expected = [5,3]
    assert arrayChange(nums, operations) == expected, "Chained replacement failed"