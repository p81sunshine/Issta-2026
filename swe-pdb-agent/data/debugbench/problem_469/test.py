from solution import *

def test_example_1():
    assert findKthBit(3, 1) == '0', "Example 1 failed"

def test_example_2():
    assert findKthBit(4, 11) == '1', "Example 2 failed"

def test_bug_case_1():
    assert findKthBit(3, 5) == '0', "Bug case 1 failed"

def test_bug_case_2():
    assert findKthBit(3, 6) == '0', "Bug case 2 failed"

def test_bug_case_3():
    assert findKthBit(4, 9) == '0', "Bug case 3 failed"