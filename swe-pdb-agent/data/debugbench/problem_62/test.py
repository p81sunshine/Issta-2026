from solution import *

def test_example_1():
    assert numMovesStonesII([7,4,9]) == [1,2], "Example 1: [7,4,9] should return [1,2]"

def test_example_2():
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Example 2: [6,5,4,3,10] should return [2,3]"

def test_all_consecutive():
    assert numMovesStonesII([1,2,3,4,5]) == [0,0], "All consecutive stones should return [0,0]"

def test_two_stones():
    assert numMovesStonesII([1,3]) == [0,0], "Two stones case should return [0,0]"

def test_large_gap_case():
    assert numMovesStonesII([1,3,5,7]) == [2,2], "Large gap case [1,3,5,7] should return [2,2]"