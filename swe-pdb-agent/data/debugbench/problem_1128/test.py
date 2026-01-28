from solution import *

def test_example_1():
    assert findValueOfPartition([1,3,2,4]) == 1, "Test case 1 failed: expected output 1"

def test_example_2():
    assert findValueOfPartition([100,1,10]) == 9, "Test case 2 failed: expected output 9"

def test_small_case():
    assert findValueOfPartition([1,2]) == 1, "Small case failed: expected 1"

def test_len_3_case():
    assert findValueOfPartition([3,1,2]) == 1, "Test for len 3 array failed"

def test_all_same():
    assert findValueOfPartition([5,5,5]) == 0, "Test for all same elements failed"