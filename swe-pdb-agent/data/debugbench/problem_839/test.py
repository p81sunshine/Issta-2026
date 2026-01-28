from solution import *

def test_example_1():
    assert arrangeWords("Leetcode is cool") == "Is cool leetcode", "Test Case 1 Failed"

def test_example_2():
    assert arrangeWords("Keep calm and code on") == "On and keep calm code", "Test Case 2 Failed"

def test_example_3():
    assert arrangeWords("To be or not to be") == "To be or to be not", "Test Case 3 Failed"

def test_empty_string():
    assert arrangeWords("") == "", "Empty string input should return empty string"

def test_single_word():
    assert arrangeWords("hello") == "Hello", "Single word should be capitalized"

def test_tie_preserves_order():
    assert arrangeWords("an a the") == "A an the", "Tied word lengths should preserve original order"

def test_capitalization_case():
    assert arrangeWords("LEETCODE is COOL") == "Is cool leetcode", "Capitalization should normalize after sorting"