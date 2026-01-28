from solution import *

def test_example_1():
    assert minSpeedOnTime([1,3,2], 6.0) == 1, "Example 1 failed"

def test_example_2():
    assert minSpeedOnTime([1,3,2], 2.7) == 3, "Example 2 failed"

def test_example_3():
    assert minSpeedOnTime([1,3,2], 1.9) == -1, "Example 3 failed"

def test_case_len_2_hour_2_0():
    assert minSpeedOnTime([1, 1], 2.0) == 1, "Case where len(dist)=2 and hour=2.0 failed"

def test_case_two_trains():
    assert minSpeedOnTime([5, 5], 2.0) == 5, "Case where two trains require exact speed failed"