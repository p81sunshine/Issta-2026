from solution import *

def test_example_1():
    assert addNegabinary([1,1,1,1,1], [1,0,1]) == [1,0,0,0,0], "First example failed"

def test_example_2():
    assert addNegabinary([0], [0]) == [0], "Second example failed"

def test_example_3():
    assert addNegabinary([0], [1]) == [1], "Third example failed"

def test_additional_case():
    assert addNegabinary([1], [1]) == [1,1,0], "Additional test case for reversal failed"