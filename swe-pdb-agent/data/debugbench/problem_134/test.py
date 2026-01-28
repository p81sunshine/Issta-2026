from solution import *

def test_example_1():
    assert averageValue([1,3,6,10,12,15]) == 9, "Should compute average of 6 and 12 correctly"

def test_example_2():
    assert averageValue([1,2,4,7,10]) == 0, "Should return 0 when no numbers divisible by 6"

def test_single_element():
    assert averageValue([6]) == 6, "Should return the single number divisible by 6"

def test_zero_value():
    assert averageValue([0]) == 0, "Zero is divisible by 6 and should return itself"

def test_multiple_values():
    assert averageValue([6, 12, 18]) == 12, "Should compute average of three numbers divisible by 6"