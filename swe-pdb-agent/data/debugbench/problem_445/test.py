from solution import *

def test_example_1():
    assert numMovesStonesII([7,4,9]) == [1,2], "Failed for example 1"

def test_example_2():
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Failed for example 2"

def test_consecutive_stones():
    assert numMovesStonesII([1,2,3]) == [0,0], "Failed for consecutive stones"

def test_two_stones():
    assert numMovesStonesII([1,5]) == [0,0], "Failed for two stones case"

def test_large_gap():
    assert numMovesStonesII([1,10,12,13]) == [1,9], "Failed for large gap scenario"