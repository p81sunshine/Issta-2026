from solution import *

def test_example_2():
    assert minSpeedOnTime([1,3,2], 2.7) == 3, "Buggy code returns -1 due to incorrect initial condition check"

def test_case_3_hour_2_5():
    assert minSpeedOnTime([1,1,1], 2.5) == 2, "Buggy code incorrectly returns -1 because of faulty initial condition"

def test_case_two_trains_1_9():
    assert minSpeedOnTime([1,1], 1.9) == 2, "Buggy code returns -1 due to incorrect hour comparison logic"

def test_single_train():
    assert minSpeedOnTime([10], 1.0) == 10, "Valid case with single train and exact hour"

def test_example_3():
    assert minSpeedOnTime([1,3,2], 1.9) == -1, "Impossible case due to insufficient time"