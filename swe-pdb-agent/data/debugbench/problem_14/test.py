from solution import *

def test_example_1():
    assert canEat([7,4,5,3,8], [[0,2,2],[4,2,4],[2,13,1000000000]]) == [True, False, True], "Example 1 failed"

def test_example_2():
    assert canEat([5,2,6,4,1], [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]) == [False,True,True,False,False], "Example 2 failed"

def test_edge_case_t0():
    assert canEat([1], [[0,0,1]]) == [True], "Edge case t=0 failed"

def test_buggy_case_t1():
    assert canEat([5,2], [[1,2,1]]) == [False], "Buggy logic scenario failed"

def test_edge_day_limit():
    assert canEat([3], [[0,2,1]]) == [True], "Day within limit failed"
    assert canEat([3], [[0,3,1]]) == [False], "Day exceeding limit failed"