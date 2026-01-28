from solution import *

def test_example_1():
    assert uniqueOccurrences([1,2,2,1,1,3]) is True, "Example 1 failed"

def test_example_2():
    assert uniqueOccurrences([1,2]) is False, "Example 2 failed"

def test_example_3():
    assert uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) is True, "Example 3 failed"

def test_duplicate_counts():
    assert uniqueOccurrences([1,1,2,2]) is False, "Test case with duplicate counts failed"