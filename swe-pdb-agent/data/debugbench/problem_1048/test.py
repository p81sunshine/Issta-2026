from solution import *

def test_example_1():
    assert lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9], "Failed for n=13"

def test_example_2():
    assert lexicalOrder(2) == [1,2], "Failed for n=2"

def test_case_n_10():
    assert lexicalOrder(10) == [1,10,2,3,4,5,6,7,8,9], "Failed for n=10"

def test_edge_case_n_1():
    assert lexicalOrder(1) == [1], "Failed for n=1"

def test_case_n_21():
    expected = [1,10,11,12,13,14,15,16,17,18,19,2,20,21,3,4,5,6,7,8,9]
    assert lexicalOrder(21) == expected, "Failed for n=21"