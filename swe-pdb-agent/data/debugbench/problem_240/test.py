from solution import *

def test_example_1():
    assert numMovesStonesII([7,4,9]) == [1,2], "Example 1 failed"

def test_example_2():
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Example 2 failed"

def test_perfect_sequence():
    assert numMovesStonesII([1,2,3]) == [0,0], "Perfect sequence test failed"

def test_partial_gap():
    assert numMovesStonesII([1,2,4]) == [1,1], "Partial gap test failed"

def test_four_stones():
    assert numMovesStonesII([1,3,5,7]) == [2,2], "Four stones test failed"