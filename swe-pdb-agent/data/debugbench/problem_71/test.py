from solution import *

def test_example_1():
    assert findKthPositive([2,3,4,7,11], 5) == 9, "Example 1: 5th missing is 9"

def test_example_2():
    assert findKthPositive([1,2,3,4], 2) == 6, "Example 2: 2nd missing is 6"

def test_empty_array():
    assert findKthPositive([], 3) == 3, "Empty array case: return k directly"

def test_missing_at_beginning():
    assert findKthPositive([3], 1) == 1, "First missing number is 1"

def test_partial_missing():
    assert findKthPositive([1,3], 1) == 2, "Single missing number in array"