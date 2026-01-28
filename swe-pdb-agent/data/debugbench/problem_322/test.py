from solution import *

def test_example_1():
    assert ways(["A..","AAA","..."], 3) == 3, "First example should return 3"

def test_example_2():
    assert ways(["A..","AA.","..."], 3) == 1, "Second example should return 1"

def test_example_3():
    assert ways(["A..","A..","..."], 1) == 1, "Third example should return 1"

def test_case_k_2():
    assert ways(["A..","A..","..."], 2) == 1, "Test case with k=2 should return 1"