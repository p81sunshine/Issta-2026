from solution import *

def test_example_1():
    assert capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title", "Example 1 failed"

def test_example_2():
    assert capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word", "Example 2 failed"

def test_example_3():
    assert capitalizeTitle("i lOve leetcode") == "i Love Leetcode", "Example 3 failed"

def test_edge_case_two_letter_word():
    assert capitalizeTitle("aB cD") == "ab cd", "Two-letter word handling failed"

def test_edge_exact_two_letters():
    assert capitalizeTitle("id") == "id", "Exact two-letter word handling failed"