from solution import *

def test_example_1():
    assert calPoints(["5","2","C","D","+"]) == 30, "Failed for example 1"

def test_example_2():
    assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27, "Failed for example 2"

def test_example_3():
    assert calPoints(["1","C"]) == 0, "Failed for example 3"

def test_empty_operations():
    assert calPoints([]) == 0, "Failed for empty operations"