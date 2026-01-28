from solution import *

def test_example_1():
    assert slidingPuzzle([[1,2,3],[4,0,5]]) == 1, "Example 1 failed"

def test_example_2():
    assert slidingPuzzle([[1,2,3],[5,4,0]]) == -1, "Example 2 failed"

def test_example_3():
    assert slidingPuzzle([[4,1,2],[5,0,3]]) == 5, "Example 3 failed"

def test_already_solved():
    assert slidingPuzzle([[1,2,3],[4,5,0]]) == 0, "Already solved case failed"