from solution import *

def test_example_1():
    assert numMovesStonesII([7,4,9]) == [1,2], "Example 1 failed"

def test_example_2():
    assert numMovesStonesII([6,5,4,3,10]) == [2,3], "Example 2 failed"

def test_all_zero_case():
    assert numMovesStonesII([1,2,3]) == [0,0], "All zeros case failed"

def test_one_zero_case():
    assert numMovesStonesII([1,2,4]) == [1,1], "One zero case failed"

def test_another_edge_case():
    assert numMovesStonesII([1,3,4]) == [1,1], "Another edge case failed"