from solution import *

def test_example_1():
    assert arrayRankTransform([40,10,20,30]) == [4,1,2,3], "Example 1 failed"

def test_example_2():
    assert arrayRankTransform([100,100,100]) == [1,1,1], "Example 2 failed"

def test_example_3():
    assert arrayRankTransform([37,12,28,9,100,56,80,5,12]) == [5,3,4,2,8,6,7,1,3], "Example 3 failed"

def test_duplicate_and_unique():
    assert arrayRankTransform([5,3,3,5]) == [2,1,1,2], "Duplicate and unique elements test failed"

def test_edge_two_duplicates():
    assert arrayRankTransform([2,2]) == [1,1], "Edge case with two duplicates failed"