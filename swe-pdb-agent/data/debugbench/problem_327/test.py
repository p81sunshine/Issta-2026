from solution import *

def test_example_1():
    assert numMovesStonesII([7,4,9]) == [1,2], "Failed for example 1"

def test_example_2():
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Failed for example 2"

def test_case_3():
    assert numMovesStonesII([1,3,4]) == [1,1], "Failed for case where move_penultimate is zero"

def test_case_4():
    assert numMovesStonesII([2,3,5]) == [1,1], "Failed for another edge case with one zero move"

def test_case_5():
    assert numMovesStonesII([1,2,3]) == [0,0], "Failed for fully packed stones"