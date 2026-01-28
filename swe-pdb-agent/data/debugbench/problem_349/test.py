from solution import *

def test_example_1():
    assert restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Failed for example 1"

def test_example_2():
    assert restoreIpAddresses("0000") == ["0.0.0.0"], "Failed for example 2"

def test_example_3():
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert restoreIpAddresses("101023") == expected, "Failed for example 3"

def test_edge_case_short_string():
    assert restoreIpAddresses("123") == [], "Failed for short string case"

def test_edge_case_empty_string():
    assert restoreIpAddresses("") == [], "Failed for empty string case"