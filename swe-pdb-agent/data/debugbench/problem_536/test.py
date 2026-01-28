from solution import *

def test_example_1():
    assert alternateDigitSum(521) == 4, "Test case 1 failed: 5-2+1 should equal 4"

def test_example_2():
    assert alternateDigitSum(111) == 1, "Test case 2 failed: 1-1+1 should equal 1"

def test_example_3():
    assert alternateDigitSum(886996) == 0, "Test case 3 failed: 8-8+6-9+9-6 should equal 0"

def test_two_digit_number():
    assert alternateDigitSum(21) == 1, "Two-digit test failed: 2-1 should equal 1"

def test_all_same_digits_even_length():
    assert alternateDigitSum(2222) == 0, "Even-length same digits test failed: 2-2+2-2 should equal 0"