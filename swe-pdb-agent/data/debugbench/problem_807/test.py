from solution import *

def test_example_1():
    actual = restoreIpAddresses("25525511135")
    expected = ["255.255.11.135", "255.255.111.35"]
    assert actual == expected, "Example 1 failed"

def test_example_2():
    actual = restoreIpAddresses("0000")
    expected = ["0.0.0.0"]
    assert actual == expected, "Example 2 failed"

def test_example_3():
    actual = restoreIpAddresses("101023")
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert actual == expected, "Example 3 failed"

def test_edge_case_short_string():
    assert restoreIpAddresses("111") == [], "Edge case with short string failed"

def test_edge_case_another_short():
    assert restoreIpAddresses("123") == [], "Another short string edge case failed"