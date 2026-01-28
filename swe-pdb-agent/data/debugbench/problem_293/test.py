from solution import *

def test_example_1():
    input_str = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    actual = restoreIpAddresses(input_str)
    assert sorted(actual) == sorted(expected), f"Example 1 failed: {actual}"

def test_example_2():
    input_str = "0000"
    expected = ["0.0.0.0"]
    actual = restoreIpAddresses(input_str)
    assert actual == expected, f"Example 2 failed: {actual}"

def test_example_3():
    input_str = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    actual = restoreIpAddresses(input_str)
    assert sorted(actual) == sorted(expected), f"Example 3 failed: {actual}"

def test_edge_case_invalid_length():
    input_str = "00000"
    expected = []
    actual = restoreIpAddresses(input_str)
    assert actual == expected, f"Edge case failed: {actual}"