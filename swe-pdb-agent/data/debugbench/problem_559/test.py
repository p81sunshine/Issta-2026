from solution import *

def test_example_1():
    assert ways(["A..","AAA","..."], 3) == 3, "Example 1 should return 3 valid ways"

def test_example_2():
    assert ways(["A..","AA.","..."], 3) == 1, "Example 2 should return 1 valid way"

def test_example_3():
    assert ways(["A..","A..","..."], 1) == 1, "Example 3 should return 1 valid way when k=1"

def test_insufficient_apples():
    assert ways(["A..","...", "..."], 3) == 0, "Should return 0 when total apples < k"

def test_single_cell():
    assert ways(["A"], 1) == 1, "Single cell with apple and k=1 should return 1"