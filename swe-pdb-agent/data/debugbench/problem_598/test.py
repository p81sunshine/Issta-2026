from solution import *

def test_example_1():
    assert min_eating_speed([3,6,7,11], 8) == 4, "Example 1 should return 4"

def test_example_2():
    assert min_eating_speed([30,11,23,4,20], 5) == 30, "Example 2 should return 30"

def test_example_3():
    assert min_eating_speed([30,11,23,4,20], 6) == 23, "Example 3 should return 23"

def test_single_pile():
    assert min_eating_speed([10], 1) == 10, "Single pile with h=1 should return 10"

def test_large_h():
    assert min_eating_speed([10, 20, 30], 100) == 1, "Large h should return minimal speed 1"