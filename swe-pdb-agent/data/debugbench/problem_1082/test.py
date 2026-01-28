from solution import *

def test_example_1():
    assert decodeCiphertext("ch   ie   pr", 3) == "cipher"

def test_example_2():
    assert decodeCiphertext("iveo    eed   l te   olc", 4) == "i love leetcode"

def test_example_3():
    assert decodeCiphertext("coding", 1) == "coding"

def test_synthetic_bug_case():
    assert decodeCiphertext("abcdef", 2) == "aebfc"

def test_edge_case_zero_trailing_spaces():
    # Test case where trailing spaces from rstrip() are important
    assert decodeCiphertext("a  b  c", 3) == "abc"