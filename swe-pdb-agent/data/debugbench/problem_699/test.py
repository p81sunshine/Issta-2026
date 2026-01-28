from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    assert restoreIpAddresses(s) == expected, "Failed for input '25525511135'"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    assert restoreIpAddresses(s) == expected, "Failed for input '0000'"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert restoreIpAddresses(s) == expected, "Failed for input '101023'"

def test_edge_case_short_string():
    s = "123"
    expected = []
    assert restoreIpAddresses(s) == expected, "Failed for short string '123'"

def test_edge_case_12345():
    s = "12345"
    expected = ["1.2.3.45", "1.2.34.5", "1.23.4.5", "12.3.4.5"]
    assert restoreIpAddresses(s) == expected, "Failed for input '12345'"