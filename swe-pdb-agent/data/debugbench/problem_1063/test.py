from solution import *

def test_example_1():
    assert minimumOperations([1,5,0,3,5]) == 3, "Example 1: Should count 1,3,5 as unique non-zero elements"

def test_example_2():
    assert minimumOperations([0]) == 0, "Example 2: Zero elements to process"

def test_no_zeros_case():
    assert minimumOperations([2,4,4,6]) == 3, "No zeros in input, all values are non-zero and unique"

def test_all_non_zero_duplicates():
    assert minimumOperations([2,2,2]) == 1, "All same non-zero elements, should count as 1 unique"