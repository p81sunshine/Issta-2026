from solution import *

def test_example_1():
    assert valid_partition([4,4,4,5,6]) == True, "Example 1 should return True"

def test_example_2():
    assert valid_partition([1,1,1,2]) == False, "Example 2 should return False"

def test_valid_pair():
    assert valid_partition([2,2]) == True, "Valid pair should return True"

def test_valid_triplet():
    assert valid_partition([3,3,3]) == True, "Valid triplet should return True"

def test_valid_consecutive_triplet():
    assert valid_partition([1,2,3]) == True, "Valid consecutive triplet should return True"