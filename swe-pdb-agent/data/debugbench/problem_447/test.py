from solution import *

def test_example_1():
    assert maximumNumber("132", [9,8,5,0,3,6,4,2,6,8]) == "832"

def test_example_2():
    assert maximumNumber("021", [9,4,3,5,7,2,1,9,0,6]) == "934"

def test_example_3():
    assert maximumNumber("5", [1,4,7,5,3,2,5,6,9,4]) == "5"

def test_buggy_logic_case():
    change = [0, 0, 0, 0, 4, 0, 0, 0, 0, 0]
    assert maximumNumber("3", change) == "3", "Buggy code would incorrectly replace 3 with 0"