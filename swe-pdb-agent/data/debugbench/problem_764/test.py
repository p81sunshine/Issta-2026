from solution import *

def test_example_1():
    assert maximumNumber("132", [9,8,5,0,3,6,4,2,6,8]) == "832", "First example failed"

def test_example_2():
    assert maximumNumber("021", [9,4,3,5,7,2,1,9,0,6]) == "934", "Second example failed"

def test_example_3():
    assert maximumNumber("5", [1,4,7,5,3,2,5,6,9,4]) == "5", "Third example failed"

def test_all_replacements():
    assert maximumNumber("111", [2]*10) == "222", "All digits should be replaced"

def test_no_replacements_needed():
    assert maximumNumber("123", [0]*10) == "123", "No replacements should occur"