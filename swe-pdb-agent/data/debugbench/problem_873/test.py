from solution import *

def test_example_1():
    assert addNegabinary([1,1,1,1,1], [1,0,1]) == [1,0,0,0,0], "Failed for example 1"

def test_example_2():
    assert addNegabinary([0], [0]) == [0], "Failed for example 2"

def test_example_3():
    assert addNegabinary([0], [1]) == [1], "Failed for example 3"

def test_add_binary_case():
    assert addBinary([1,1], [1]) == [1,0,0], "Failed binary addition with carry"

def test_add_binary_edge_case():
    assert addBinary([1], [1]) == [1,0], "Failed binary addition edge case"