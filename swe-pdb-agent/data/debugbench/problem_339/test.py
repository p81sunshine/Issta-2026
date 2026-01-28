from solution import *

def test_example_1():
    assert calPoints(["5","2","C","D","+"]) == 30

def test_example_2():
    assert calPoints(["5","-2","4","C","D","9","+","+"]) == 27

def test_example_3():
    assert calPoints(["1","C"]) == 0

def test_empty_input():
    assert calPoints([]) == 0

def test_single_operation():
    assert calPoints(["3"]) == 3