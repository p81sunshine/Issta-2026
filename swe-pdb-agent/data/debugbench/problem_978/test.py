from solution import *

def test_example_1():
    encoded_text = "ch   ie   pr"
    rows = 3
    expected = "cipher"
    result = decodeCiphertext(encoded_text, rows)
    assert result == expected, f"Expected '{expected}' but got '{result}'"

def test_example_2():
    encoded_text = "iveo    eed   l te   olc"
    rows = 4
    expected = "i love leetcode"
    result = decodeCiphertext(encoded_text, rows)
    assert result == expected, f"Expected '{expected}' but got '{result}'"

def test_example_3():
    encoded_text = "coding"
    rows = 1
    expected = "coding"
    result = decodeCiphertext(encoded_text, rows)
    assert result == expected, f"Expected '{expected}' but got '{result}'"

def test_single_row_edge_case():
    encoded_text = "pytest"
    rows = 1
    expected = "pytest"
    result = decodeCiphertext(encoded_text, rows)
    assert result == expected, f"Failed for single row case: expected '{expected}'"

def test_empty_string_input():
    encoded_text = ""
    rows = 1
    expected = ""
    result = decodeCiphertext(encoded_text, rows)
    assert result == expected, f"Failed for empty input: expected '{expected}'"