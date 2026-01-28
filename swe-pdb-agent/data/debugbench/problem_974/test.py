from solution import *

def test_example_2():
    assert minSpeedOnTime([1,3,2], 2.7) == 3, "Test case 2 failed"

def test_case_1_1_1_4_0():
    assert minSpeedOnTime([1,1,1], 4.0) == 1, "Test case with len 3 and hour 4.0 failed"

def test_case_1_1_2_0():
    assert minSpeedOnTime([1,1], 2.0) == 1, "Test case len 2, hour 2.0 failed"

def test_case_3_4_3_0():
    assert minSpeedOnTime([3,4], 3.0) == 3, "Test case [3,4], 3.0 failed"