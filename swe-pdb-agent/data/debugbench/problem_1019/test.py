from solution import *

def test_example_1():
    assert maxPower([1,2,4,5,0], 1, 2) == 5, "Example 1 failed"

def test_example_2():
    assert maxPower([4,4,4,4], 0, 3) == 4, "Example 2 failed"

def test_addition_operation():
    assert maxPower([3, 1], 0, 1) == 2, "Addition operation bug not caught"

def test_indexing_error():
    assert maxPower([1, 1], 1, 0) == 2, "Indexing error not caught"

def test_single_station():
    assert maxPower([1], 0, 1) == 2, "Single station case failed"