from solution import *

def test_example_1():
    assert lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9], "Failed for input n=13"

def test_example_2():
    assert lexicalOrder(2) == [1,2], "Failed for input n=2"

def test_edge_case_n1():
    assert lexicalOrder(1) == [1], "Failed for edge case n=1"

def test_edge_case_n3():
    assert lexicalOrder(3) == [1,2,3], "Failed for input n=3"