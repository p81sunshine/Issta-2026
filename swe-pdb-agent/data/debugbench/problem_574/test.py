from solution import *

def test_example_1():
    assert sliding_puzzle([[1,2,3],[4,0,5]]) == 1, "Input [[1,2,3],[4,0,5]] should return 1"

def test_example_2():
    assert sliding_puzzle([[1,2,3],[5,4,0]]) == -1, "Input [[1,2,3],[5,4,0]] should return -1"

def test_example_3():
    assert sliding_puzzle([[4,1,2],[5,0,3]]) == 5, "Input [[4,1,2],[5,0,3]] should return 5"

def test_edge_case_solved():
    assert sliding_puzzle([[1,2,3],[4,5,0]]) == 0, "Solved board should return 0 moves"