from solution import *

def test_example_1():
    assert numMovesStonesII([7,4,9]) == [1,2], "Test case 1 failed"

def test_example_2():
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Test case 2 failed"

def test_case_3():
    assert numMovesStonesII([1,3,6]) == [1,2], "Test case 3 failed"

def test_consecutive_stones():
    assert numMovesStonesII([1,2,3]) == [0,0], "Consecutive stones test failed"