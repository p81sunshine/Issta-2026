from solution import *

def test_example_1():
    assert validPartition([4,4,4,5,6]) is True, "Valid partition should be true for [4,4,4,5,6]"

def test_example_2():
    assert validPartition([1,1,1,2]) is False, "Valid partition should be false for [1,1,1,2]"

def test_consecutive_sequence():
    assert validPartition([3,4,5]) is True, "Valid partition should be true for consecutive sequence [3,4,5]"

def test_another_consecutive_sequence():
    assert validPartition([5,6,7]) is True, "Valid partition should be true for consecutive sequence [5,6,7]"

def test_edge_case_single_triple():
    assert validPartition([1,1,1]) is True, "Valid partition should be true for triple [1,1,1]"