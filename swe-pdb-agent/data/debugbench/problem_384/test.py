from solution import *

def test_example_1():
    assert arrangeWords("Leetcode is cool") == "Is cool leetcode", "Failed for example 1"

def test_example_2():
    assert arrangeWords("Keep calm and code on") == "On and keep calm code", "Failed for example 2"

def test_example_3():
    assert arrangeWords("To be or not to be") == "To be or to be not", "Failed for example 3"

def test_same_length_words():
    assert arrangeWords("baa aab abb") == "Baa aab abb", "Failed for same-length words preservation"

def test_empty_input():
    assert arrangeWords("") == "", "Failed for empty input"