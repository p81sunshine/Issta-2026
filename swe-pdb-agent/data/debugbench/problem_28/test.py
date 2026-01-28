from solution import *

def test_example_1():
    assert find_complement(5) == 2, "Example 1 failed"

def test_example_2():
    assert find_complement(1) == 0, "Example 2 failed"

def test_case_num_2():
    assert find_complement(2) == 1, "Test case num=2 failed"

def test_case_num_7():
    assert find_complement(7) == 0, "Test case num=7 failed"

def test_case_num_3():
    assert find_complement(3) == 0, "Test case num=3 failed"