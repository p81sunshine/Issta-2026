from solution import *

def test_example_1():
    ops = ["5","2","C","D","+"]
    assert calPoints(ops) == 30, "Failed for example 1: sum of [5, 10, 15] should be 30"

def test_example_2():
    ops = ["5","-2","4","C","D","9","+","+"]
    assert calPoints(ops) == 27, "Failed for example 2: sum of [5, -2, -4, 9, 5, 14] should be 27"

def test_example_3():
    ops = ["1","C"]
    assert calPoints(ops) == 0, "Failed for example 3: empty stack should return 0"

def test_multiple_elements():
    ops = ["5", "2"]
    assert calPoints(ops) == 7, "Failed for two elements: sum of [5, 2] should be 7"

def test_plus_operation():
    ops = ["5", "2", "+"]
    assert calPoints(ops) == 14, "Failed for '+' operation: sum of [5, 2, 7] should be 14"