from solution import *

def test_example_1():
    assert ways(["A..","AAA","..."], 3) == 3, "Example 1 failed"

def test_example_2():
    assert ways(["A..","AA.","..."], 3) == 1, "Example 2 failed"

def test_example_3():
    assert ways(["A..","A..","..."], 1) == 1, "Example 3 failed"

def test_insufficient_apples():
    assert ways(["A..","...", "..."], 2) == 0, "Insufficient apples test failed"

def test_single_cell():
    assert ways(["A"], 1) == 1, "Single cell with apple failed"
    assert ways(["."], 1) == 0, "Single cell without apple failed"