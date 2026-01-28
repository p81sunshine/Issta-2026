from solution import *

def test_example_1():
    assert alternateDigitSum(521) == 4, "Test case 1 failed: 521 should return 4"

def test_example_2():
    assert alternateDigitSum(111) == 1, "Test case 2 failed: 111 should return 1"

def test_example_3():
    assert alternateDigitSum(886996) == 0, "Test case 3 failed: 886996 should return 0"

def test_edge_two_digits():
    assert alternateDigitSum(12) == -1, "Edge case 12 should return -1"

def test_three_digits_case():
    assert alternateDigitSum(123) == 2, "123 should return 2 (1 -2 +3)"