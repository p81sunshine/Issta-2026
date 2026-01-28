from solution import *

def test_example_1():
    assert restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"], "Example 1 failed"

def test_example_2():
    assert restoreIpAddresses("0000") == ["0.0.0.0"], "Example 2 failed"

def test_example_3():
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert restoreIpAddresses("101023") == expected, "Example 3 failed"

def test_invalid_input():
    assert restoreIpAddresses("0") == [], "Invalid input test failed"

def test_edge_case_short():
    assert restoreIpAddresses("111") == [], "Edge case with short string failed"

def test_valid_input_1111():
    assert restoreIpAddresses("1111") == ["1.1.1.1"], "Valid 1111 test failed"