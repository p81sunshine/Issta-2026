from solution import *

def test_example_1():
    assert alternate_digit_sum(521) == 4, "Example 1 failed: should be 5-2+1=4"

def test_example_2():
    assert alternate_digit_sum(111) == 1, "Example 2 failed: should be 1-1+1=1"

def test_example_3():
    assert alternate_digit_sum(886996) == 0, "Example 3 failed: should be 8-8+6-9+9-6=0"

def test_two_digit_number():
    assert alternate_digit_sum(12) == -1, "Two-digit case failed: should be 1-2=-1"