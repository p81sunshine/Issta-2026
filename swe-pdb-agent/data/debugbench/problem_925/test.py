from solution import *

def test_example_1():
    assert maxDistance([1,1,1,6,1,1,1]) == 3, "Test case 1 failed"

def test_example_2():
    assert maxDistance([1,8,3,8,3]) == 4, "Test case 2 failed"

def test_example_3():
    assert maxDistance([0,1]) == 1, "Test case 3 failed"

def test_all_same_colors():
    assert maxDistance([5,5,5]) == 0, "All same colors edge case failed"

def test_first_last_different():
    assert maxDistance([3,4,3,3,3]) == 3, "First/last different edge case failed"