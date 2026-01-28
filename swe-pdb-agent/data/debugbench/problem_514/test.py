from solution import *

def test_example_1():
    nums = ["3","6","7","10"]
    k = 4
    assert kthLargestNumber(nums, k) == "3", "Failed for 4th largest in [3,6,7,10]"

def test_example_2():
    nums = ["2","21","12","1"]
    k = 3
    assert kthLargestNumber(nums, k) == "2", "Failed for 3rd largest in [2,21,12,1]"

def test_example_3():
    nums = ["0","0"]
    k = 2
    assert kthLargestNumber(nums, k) == "0", "Failed for 2nd largest in [0,0]"

def test_k_equals_1():
    nums = ["5","9","1"]
    k = 1
    assert kthLargestNumber(nums, k) == "9", "Failed for 1st largest in [5,9,1]"