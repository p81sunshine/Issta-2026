from solution import *

def test_example_1():
    assert countPairs([3,1,2,2,2,1,3], 2) == 4, "Example 1 should return 4 valid pairs"

def test_example_2():
    assert countPairs([1,2,3,4], 1) == 0, "Example 2 should return 0 as no duplicates exist"

def test_indices_over_values():
    assert countPairs([3,3], 5) == 1, "Indices product (0*1=0) is divisible by 5, but values product (3*3=9) is not"

def test_multiple_indices():
    assert countPairs([1,1,1], 2) == 3, "All 3 pairs (0,1), (0,2), (1,2) have index products divisible by 2"