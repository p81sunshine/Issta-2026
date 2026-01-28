from solution import *

def test_example_1():
    assert addNegabinary([1,1,1,1,1], [1,0,1]) == [1,0,0,0,0], "Example 1 failed"

def test_example_2():
    assert addNegabinary([0], [0]) == [0], "Example 2 failed"

def test_example_3():
    assert addNegabinary([0], [1]) == [1], "Example 3 failed"

def test_add_binary_case():
    assert addBinary([1,0], [1]) == [1,1], "AddBinary test case failed"

def test_add_negabinary_case():
    assert addNegabinary([0,1], [1]) == [1,1,0], "AddNegabinary test case failed"