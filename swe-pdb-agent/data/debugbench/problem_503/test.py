from solution import *

def test_example_1():
    assert minSubsequence([4,3,10,9,8]) == [10,9], "Failed for example 1"

def test_example_2():
    assert minSubsequence([4,4,7,6,7]) == [7,7,6], "Failed for example 2"

def test_case_3():
    assert minSubsequence([1,2,3,4,5]) == [5,4], "Failed for incremental sequence"

def test_edge_case_1():
    assert minSubsequence([2,2,2]) == [2,2], "Failed for equal elements case"

def test_edge_case_2():
    assert minSubsequence([5,1]) == [5], "Failed for two-element case"