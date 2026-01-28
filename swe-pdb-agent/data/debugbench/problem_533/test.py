from solution import *

def test_example_1():
    assert uniqueOccurrences([1,2,2,1,1,3]) is True, "Example 1 should return True"

def test_example_2():
    assert uniqueOccurrences([1,2]) is False, "Example 2 should return False"

def test_example_3():
    assert uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) is True, "Example 3 should return True"

def test_duplicate_occurrences():
    assert uniqueOccurrences([1,1,2,2,3,3]) is False, "Should detect duplicate occurrences (2, 2, 2)"

def test_mixed_occurrences():
    assert uniqueOccurrences([1,1,2,2,3]) is False, "Should detect duplicate values in occurrences (2, 2, 1)"