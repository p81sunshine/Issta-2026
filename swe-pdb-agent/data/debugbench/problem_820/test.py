from solution import *

def test_example_1():
    assert minimum_partition("165462", 60) == 4, "Example 1 failed"

def test_example_2():
    assert minimum_partition("238182", 5) == -1, "Example 2 failed"

def test_split_required():
    assert minimum_partition("638", 10) == 3, "Split required case failed"

def test_single_partition():
    assert minimum_partition("12", 50) == 1, "Single partition case failed"

def test_zero_case():
    assert minimum_partition("0", 0) == 1, "Zero case failed"