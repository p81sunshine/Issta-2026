from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    actual = restoreIpAddresses(s)
    assert actual == expected, "Failed for input '25525511135'"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    actual = restoreIpAddresses(s)
    assert actual == expected, "Failed for input '0000'"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    actual = restoreIpAddresses(s)
    assert sorted(actual) == sorted(expected), "Failed for input '101023'"

def test_edge_case_length_3():
    s = "123"
    expected = []
    actual = restoreIpAddresses(s)
    assert actual == expected, "Failed for input with length 3"