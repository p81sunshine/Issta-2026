from solution import *

def test_example_1():
    assert decodeCiphertext("ch   ie   pr", 3) == "cipher", "Failed for example 1"

def test_example_2():
    assert decodeCiphertext("iveo    eed   l te   olc", 4) == "i love leetcode", "Failed for example 2"

def test_example_3():
    assert decodeCiphertext("coding", 1) == "coding", "Failed for example 3"

def test_edge_case_empty_string():
    assert decodeCiphertext("", 1) == "", "Failed for empty string case"