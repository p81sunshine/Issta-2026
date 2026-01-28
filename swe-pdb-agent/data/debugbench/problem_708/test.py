from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Example 1 failed: Input 5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Example 2 failed: Input 1 should return 0"

def test_additional_case_1():
    assert findComplement(2) == 1, "Test case failed: Input 2 should return 1 (binary 10 → 01=1)"

def test_additional_case_2():
    assert findComplement(4) == 3, "Test case failed: Input 4 should return 3 (binary 100 → 011=3)"

def test_additional_case_3():
    assert findComplement(6) == 1, "Test case failed: Input 6 should return 1 (binary 110 → 001=1)"