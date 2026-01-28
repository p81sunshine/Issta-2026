from solution import *

def test_example_1():
    assert alternateDigitSum(521) == 4, "Failed for input 521"

def test_example_2():
    assert alternateDigitSum(111) == 1, "Failed for input 111"

def test_example_3():
    assert alternateDigitSum(886996) == 0, "Failed for input 886996"

def test_alternating_pattern():
    assert alternateDigitSum(121) == 0, "Failed for alternating pattern 121"
    assert alternateDigitSum(99) == 0, "Failed for two-digit alternating case"