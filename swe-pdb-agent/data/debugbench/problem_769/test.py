from solution import *

def test_example_1():
    assert restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"], "Example 1 failed"

def test_example_2():
    assert restoreIpAddresses("0000") == ["0.0.0.0"], "Example 2 failed"

def test_example_3():
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert restoreIpAddresses("101023") == expected, "Example 3 failed"

def test_edge_case_short_input():
    assert restoreIpAddresses("123") == [], "Short input should return empty list"

def test_edge_case_max_length():
    assert restoreIpAddresses("255255255255") == ["255.255.255.255"], "Max length input failed"