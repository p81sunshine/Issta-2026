from solution import *

def test_example_1():
    assert largestInteger(1234) == 3412, "Example 1 failed"

def test_example_2():
    assert largestInteger(65875) == 87655, "Example 2 failed"

def test_even_heap_required():
    assert largestInteger(246) == 642, "Test even digits requiring heapify failed"

def test_odd_heap_required():
    assert largestInteger(135) == 531, "Test odd digits requiring heapify failed"

def test_single_digit():
    assert largestInteger(5) == 5, "Single digit test failed"