from solution import *

def test_example_1():
    ops = ["5","2","C","D","+"]
    assert calPoints(ops) == 30, "First example should return 30"

def test_example_2():
    ops = ["5","-2","4","C","D","9","+","+"]
    assert calPoints(ops) == 27, "Second example should return 27"

def test_example_3():
    ops = ["1","C"]
    assert calPoints(ops) == 0, "Third example should return 0"

def test_d_operation():
    ops = ["5", "D"]
    assert calPoints(ops) == 15, "5 followed by D should sum to 15"

def test_empty_after_c():
    ops = ["4", "C"]
    assert calPoints(ops) == 0, "C should clear stack and return 0 sum"