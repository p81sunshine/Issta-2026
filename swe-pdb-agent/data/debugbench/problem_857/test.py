from solution import *

def test_example_1():
    assert calPoints(["5","2","C","D","+"]) == 30, "Example 1 failed"

def test_example_2():
    assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27, "Example 2 failed"

def test_example_3():
    assert calPoints(["1","C"]) == 0, "Example 3 failed"

def test_empty_operations():
    assert calPoints([]) == 0, "Empty operations should return 0"

def test_single_number():
    assert calPoints(["3"]) == 3, "Single number should return its value"