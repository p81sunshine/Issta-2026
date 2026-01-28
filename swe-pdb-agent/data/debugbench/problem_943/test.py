from solution import *

def test_example_1():
    assert maximumNumber("132", [9,8,5,0,3,6,4,2,6,8]) == "832"

def test_example_2():
    assert maximumNumber("021", [9,4,3,5,7,2,1,9,0,6]) == "934"

def test_example_3():
    assert maximumNumber("5", [1,4,7,5,3,2,5,6,9,4]) == "5"

def test_buggy_condition_1():
    # Correct code replaces 2 with 3 (2 < change[2]=3)
    # Buggy code checks 2 < change[3]=1 → no replacement
    assert maximumNumber("2", [0,0,3,1,0,0,0,0,0,0]) == "3"

def test_buggy_condition_2():
    # Correct code: 3 is not less than change[3]=2 → no replacement
    # Buggy code checks 3 < change[4]=4 → replaces with change[3]=2
    assert maximumNumber("3", [0,0,0,2,4,0,0,0,0,0]) == "3"