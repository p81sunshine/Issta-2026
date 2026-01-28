from solution import *

def test_example_1():
    assert thirdMax([3,2,1]) == 1, "Should return 1 for [3,2,1]"

def test_example_2():
    assert thirdMax([1,2]) == 2, "Should return 2 for [1,2]"

def test_example_3():
    assert thirdMax([2,2,3,1]) == 1, "Should return 1 for [2,2,3,1]"

def test_unique_count_4():
    assert thirdMax([4,5,6,7]) == 5, "Should return 5 for [4,5,6,7] when unique count is 4"

def test_duplicate_values():
    assert thirdMax([5,5,4,4,3,3,2,2,1]) == 3, "Should return 3 for list with 5 unique elements"