from solution import *

def test_example_1():
    assert maximum_number("132", [9,8,5,0,3,6,4,2,6,8]) == "832"

def test_example_2():
    assert maximum_number("021", [9,4,3,5,7,2,1,9,0,6]) == "934"

def test_example_3():
    assert maximum_number("5", [1,4,7,5,3,2,5,6,9,4]) == "5"

def test_replacement_when_better_later():
    num = "3"
    change = [0,1,2,0,5,0,0,0,0,0]
    assert maximum_number(num, change) == "3", "Buggy code would replace with lower value"

def test_mixed_replacement():
    num = "23"
    change = [0,0,1,4,0,0,0,0,0,0]
    assert maximum_number(num, change) == "24", "Buggy code would replace first digit incorrectly"