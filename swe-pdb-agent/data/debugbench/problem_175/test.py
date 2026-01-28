from solution import *

def test_example_1():
    assert minFlips(2, 6, 5) == 3, "Example 1 failed: Expected 3 flips"

def test_example_2():
    assert minFlips(4, 2, 7) == 1, "Example 2 failed: Expected 1 flip"

def test_example_3():
    assert minFlips(1, 2, 3) == 0, "Example 3 failed: Expected 0 flips"

def test_both_ones_to_zero():
    assert minFlips(1, 1, 0) == 2, "Both a and b are 1, c is 0: Expected 2 flips"

def test_one_one_to_zero():
    assert minFlips(1, 0, 0) == 1, "a is 1, b is 0, c is 0: Expected 1 flip"