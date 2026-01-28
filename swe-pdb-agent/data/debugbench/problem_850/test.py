from solution import *

def test_example_1():
    assert ways(["A..","AAA","..."], 3) == 3, "First example should return 3"

def test_example_2():
    assert ways(["A..","AA.","..."], 3) == 1, "Second example should return 1"

def test_example_3():
    assert ways(["A..","A..","..."], 1) == 1, "Third example should return 1"

def test_no_apples():
    assert ways(["...", "..."], 1) == 0, "No apples should return 0"

def test_single_cell_with_apple():
    assert ways(["A"], 1) == 1, "Single cell with apple and k=1 should return 1"

def test_k_larger_than_apples():
    assert ways(["A.A","A..","..."], 4) == 0, "k larger than apples should return 0"