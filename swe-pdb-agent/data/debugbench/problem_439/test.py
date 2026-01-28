from solution import *

def test_example_1():
    assert minFlips(2, 6, 5) == 3, "Example 1 failed"

def test_example_2():
    assert minFlips(4, 2, 7) == 1, "Example 2 failed"

def test_example_3():
    assert minFlips(1, 2, 3) == 0, "Example 3 failed"

def test_edge_case_both_ones_to_zero():
    assert minFlips(3, 3, 0) == 4, "Edge case both ones to zero failed"

def test_edge_case_single_bit():
    assert minFlips(0, 0, 1) == 1, "Edge case single bit failed"