from solution import *

def test_example_1():
    actual = restoreIpAddresses("25525511135")
    expected = ["255.255.11.135", "255.255.111.35"]
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    actual = restoreIpAddresses("0000")
    expected = ["0.0.0.0"]
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_3():
    actual = restoreIpAddresses("101023")
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_edge_case_invalid_length():
    actual = restoreIpAddresses("000")
    expected = []
    assert actual == expected, f"Expected {expected} for short input, got {actual}"

def test_edge_case_1234():
    actual = restoreIpAddresses("1234")
    expected = ["1.2.3.4"]
    assert actual == expected, f"Expected {expected} for input '1234', got {actual}"