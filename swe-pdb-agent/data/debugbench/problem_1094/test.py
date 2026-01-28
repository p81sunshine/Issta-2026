from solution import *

def test_example_1():
    edges = [1,0,0,0,0,7,7,5]
    assert edgeScore(edges) == 7, "First example should return 7"

def test_example_2():
    edges = [2,0,0,2]
    assert edgeScore(edges) == 0, "Second example should return 0"

def test_case_3():
    edges = [0, 1]
    assert edgeScore(edges) == 1, "Test case with minimal valid input"

def test_case_4():
    edges = [0, 1, 0]
    assert edgeScore(edges) == 0, "Test case with last iteration index access"

def test_case_5():
    edges = [0, 0]
    assert edgeScore(edges) == 0, "Test case with tied scores"