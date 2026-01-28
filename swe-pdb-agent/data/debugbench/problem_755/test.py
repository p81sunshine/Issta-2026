from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Example 1 failed: Input 5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Example 2 failed: Input 1 should return 0"

def test_case_3():
    assert findComplement(2) == 1, "Test case 3 failed: Input 2 should return 1"

def test_case_4():
    assert findComplement(4) == 3, "Test case 4 failed: Input 4 should return 3"

def test_case_5():
    assert findComplement(6) == 1, "Test case 5 failed: Input 6 should return 1"