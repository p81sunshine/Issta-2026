from solution import *

def test_example_1():
    assert distributeCandies([1,1,2,2,3,3]) == 3, "Case with equal types and max capacity"

def test_example_2():
    assert distributeCandies([1,1,2,3]) == 2, "Case where types exceed max capacity"

def test_example_3():
    assert distributeCandies([6,6,6,6]) == 1, "Case with minimal unique types"

def test_edge_case_small_input():
    assert distributeCandies([1,2]) == 1, "Edge case with minimum possible input"